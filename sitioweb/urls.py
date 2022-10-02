from django.urls import path
from . import views


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros/', views.nosotros, name="nosotros"),
    #path('productos/', views.productos, name="productos"),
    path('contactenos/', views.contactenos, name="contactenos"),
    path('login/', views.iniciosesion, name="login"),
    path("signup/", views.registrarse, name="signup"),
    path("logout/", views.cerrarsesion, name="logout"),
    path('agregar/<int:producto_id>/', views.agregar_producto, name='Add'),
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name='Del'),
    path('restar/<int:producto_id>/', views.restar_producto, name='Sub'),
    path('limpiar/', views.limpiar_carrito, name='CLS'),
    path('pedidos/', views.procesar_pedido, name='procesar_pedido'),
    path("producto/<int:producto_id>/", views.ver_producto, name='ver_producto' ),
    
]