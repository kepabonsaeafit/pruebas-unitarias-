class RepositorioFake:
    def __init__(self):
        self.compras = []
    def guardar(self,usuario,cantidad):
        self.compras.append({
            "usuario": usuario,
            "cantidad": cantidad
        })              
repo = RepositorioFake()
repo.guardar("Migue", 2)
repo.guardar("Ana",3)
print (repo.compras)
