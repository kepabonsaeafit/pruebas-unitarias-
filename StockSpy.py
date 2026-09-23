class InventarioSpy:
    def __init__(self):
        self.veces_consultado = 0

    def consultar_disponibilidad(self):
        self.veces_consultado += 1
        return 50

# inventario = InventarioSpy()
# 
# inventario.consultar_disponibilidad()
# inventario.consultar_disponibilidad()
# inventario.consultar_disponibilidad()
# 
# print(inventario.veces_consultado)



