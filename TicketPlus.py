from StockPlus import InventarioStub
from UserDummy import UsuarioDummy
from FakeRepository import RepositorioFake
from EmailDummy import EmailDummy
from unittest.mock import Mock
from StockSpy import InventarioSpy

email_mock = Mock()


class TicketService:
   def __init__(self, inventario, repositorio, email_service):
      self.inventario = inventario
      self.repositorio = repositorio
      self.email_service = email_service
 
   def comprar(self, usuario, cantidad):
      disponibles = self.inventario.consultar_disponibilidad()
      if disponibles < cantidad:
          return False
      self.repositorio.guardar(usuario, cantidad)
      self.email_service.enviar_confirmacion(usuario)
      return True

inventario_spy = InventarioSpy()

service = TicketService(
   #None,
   inventario_spy,
   #InventarioStub(),
   #None,
   #UsuarioDummy(),
   RepositorioFake(),
   #None
   #EmailDummy()
   email_mock
)

service.comprar(UsuarioDummy(),1)
print(inventario_spy.veces_consultado)


