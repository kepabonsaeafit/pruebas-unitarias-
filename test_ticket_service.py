from unittest.mock import Mock

from TicketPlus import TicketService
from StockPlus import InventarioStub
from FakeRepository import RepositorioFake
from UserDummy import UsuarioDummy

def test_compra_exitosa():

    email_mock = Mock()

    service = TicketService(
        InventarioStub(),
        RepositorioFake(),
        email_mock
    )

    resultado = service.comprar(
        UsuarioDummy(),
        2
    )

    assert resultado is True

    email_mock.enviar_confirmacion.assert_called_once()
