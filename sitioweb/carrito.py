class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            carrito = self.session["carrito"] = {}
            #self.session["carrito"] = {}
            #self.carrito = self.session["carrito"]
        #else:
            #self.carrito = carrito
        self.carrito = carrito

    def agregar(self, producto):

        # if(str(producto.id) not in self.carrito.keys()):
        #     self.carrito[producto.id] = {
        #         "producto_id": producto.id,
        #         "nombre": producto.nombre,
        #         "precio": str(producto.precio),
        #         "cantidad": 1,
        #         "imagen": producto.imagen.url,
        #         "acumulado": producto.precio,

        #     }
        # else:
        #     for key, value in self.carrito.items():
        #         if key==str(producto.id):
        #             value["cantidad"] = value["cantidad"] + 1
        #             value["acumulado"] = value["acumulado"] + value["precio"]
        #             break

        # self.guardar_carrito()
        

        id = str(producto.id)
        if id not in self.carrito.keys():
            self.carrito[id]={
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio": producto.precio,
                "acumulado": producto.precio,
                "imagen": producto.imagen.url,
                "cantidad": 1,
            }
        else:
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["acumulado"] += producto.precio
            self.carrito[id]["precio"] = producto.precio
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, producto):

        producto.id = str(producto.id)

        if producto.id in self.carrito:
            del self.carrito[producto.id]
            self.guardar_carrito()

        # id = str(producto.id)
        # if id in self.carrito:
        #     del self.carrito[id]
        #     self.guardar_carrito()



    def restar(self, producto):

        # for key, value in self.carrito.items():
        #         if key==str(producto.id):
        #             value["cantidad"] = value["cantidad"] - 1
        #             value["acumulado"] = value["acumulado"] - value["precio"]
        #             if value["cantidad"] < 1:
        #                 self.eliminar(producto)
        #             break
        
        # self.guardar_carrito()
                

        id = str(producto.id)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
            self.carrito[id]["acumulado"] -= producto.precio
            if self.carrito[id]["cantidad"] <= 0: self.eliminar(producto)
            self.guardar_carrito()



    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True