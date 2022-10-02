def total_carrito(request):
    total = 0
    if request.user.is_authenticated:
        if "carrito" in request.session.keys():
            for key, value in request.session["carrito"].items():
                #total += int(value["acumulado"])
                total += float(value["precio"]*value["cantidad"])

    else:
        total = "Debes iniciar sesion para ver el carro de compras"
    
    return {"total_carrito": total}
