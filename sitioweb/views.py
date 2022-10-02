from urllib.request import Request
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from sitioweb.models import LineaPedido, Pedido, Producto
from sitioweb.carrito import Carrito

from django.contrib import messages
#from django.template.loader import render_to_string
#from django.utils.html import strip_tags
#from django.core.mail import send_mail


# Create your views here.
def inicio(request):
    productos = Producto.objects.all()
    #carrito=Carrito(Request)
    return render(request, "index.html", {"productos":productos})

def ver_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    return render(request, "producto.html", {"producto": producto,})
    

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto=producto)
    return redirect("inicio")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto=producto)
    return redirect("inicio")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto=producto)
    return redirect("inicio")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("inicio")

def nosotros(request):
    return render(request, "nosotros.html")


def contactenos(request):
    return render(request, "contactenos.html")


def iniciosesion(request):
    if request.method == "GET":

        return render(request, "iniciar_sesion.html", {
            "userLoginForm": AuthenticationForm
        })

    else:
        user = authenticate(
            request, username=request.POST["username"], password=request.POST["password"])

        if user is None:
            return render(request, "iniciar_sesion.html", {
                "userLoginForm": AuthenticationForm,
                "error": "Usuario o contraseña es incorrecta"
            })

        else:
            login(request, user)
            return redirect("inicio")

@login_required
def cerrarsesion(request):
    logout(request)
    return redirect("inicio")


def registrarse(request):
    
    if request.method == "GET":
        #print("enviando datos")
        return render(request, "registrarse.html", {
            "userCreateForm": UserCreationForm
        })
    else:
        if request.POST["password1"] == request.POST["password2"]:
            # register user
            try:
                user = User.objects.create_user(
                    username=request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                # return HttpResponse("Usuario creado satisfactoriamente")
                return redirect("inicio")

            except IntegrityError:
                return render(request, "registrarse.html", {
                    "userCreateForm": UserCreationForm,
                    "error": "El usuario ya existe"
                })

        return render(request, "registrarse.html", {
            "userCreateForm": UserCreationForm,
            "error": "Las contraseñas no coinciden"
        })


@login_required(login_url="/login/") #Por seguridad se comenta para no enviar email
def procesar_pedido(request):
    pedido = Pedido.objects.create(user=request.user)
    carro=Carrito(request)
    lineas_pedido=list()

    for key, value in carro.carrito.items():
        lineas_pedido.append(LineaPedido(

            producto_id = key,
            cantidad = value["cantidad"],
            user = request.user,
            pedido = pedido

        ))
    
    LineaPedido.objects.bulk_create(lineas_pedido)

    # enviar_mail(pedido = pedido,
    #     lineas_pedido = lineas_pedido,
    #     nombreusuario = request.user.username,
    #     emailusuario = request.user.email
    # )

    messages.success(request, "El pedido se ha creado correctamente")

    #return redirect("inicio")
    
    return render(request, "emails/pedido.html", {
        "pedido": pedido, 
        "lineas_pedido": lineas_pedido,
        "nombreusuario": request.user.username,
        "emailusuario": request.user.email,
        })

# def enviar_mail(**kwargs):
    
#     asunto = "Gracias por su pedido"
#     mensaje = render_to_string("emails/pedido.html", {
#         "pedido": kwargs.get("pedido"), 
#         "lineas_pedido": kwargs.get("lineas_pedido"),
#         "nombreusuario": kwargs.get("nombreusuario")

#     })

#     mensaje_texto = strip_tags(mensaje)
#     from_email = "contacto@leperra.com"
#     to = kwargs.get("emailusuario")

#     send_mail(asunto, mensaje_texto, from_email, [to], html_message=mensaje)