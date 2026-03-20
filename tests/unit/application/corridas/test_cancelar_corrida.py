import pytest
from src.application.corridas.cancelar_corrida import CancelarCorridaUseCase
from src.domain.corridas.entities import Corrida, StatusCorrida
from src.domain.usuarios.entities import Usuario, PapelUsuario
from src.domain.shared.value_objects import Endereco

class FakeCorridaRepo:
    def __init__(self, corrida):
        self.corrida = corrida
        self.saved = []
    def get_by_id(self, id):
        return self.corrida
    def save(self, corrida):
        self.saved.append(corrida)

@pytest.fixture
def corrida():
    cliente = Usuario(cpf="12345678900", nome="Cliente Teste", telefone_whatsapp="999999999", papeis=[PapelUsuario.CLIENTE])
    origem = Endereco("Rua A", "100", "Centro", "Cidade", "UF", "00000-000", -10.0, -20.0)
    destino = Endereco("Rua B", "200", "Bairro", "Cidade", "UF", "11111-111", -11.0, -21.0)
    return Corrida(
        id="c4",
        cliente=cliente,
        motorista=None,
        origem=origem,
        destino=destino,
        status=StatusCorrida.SOLICITADA
    )

def test_cancelar_corrida(corrida):
    repo = FakeCorridaRepo(corrida)
    usecase = CancelarCorridaUseCase(repo)
    result = usecase.execute("c4", motivo="Mudança de planos")
    assert result.status == StatusCorrida.CANCELADA_CLIENTE
    assert result.motivo_cancelamento == "Mudança de planos"
    assert repo.saved[0] == result
