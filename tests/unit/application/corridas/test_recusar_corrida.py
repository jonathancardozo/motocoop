import pytest
from src.application.corridas.recusar_corrida import RecusarCorridaUseCase
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
def motorista():
    return Usuario(cpf="11122233344", nome="Motorista Teste", telefone_whatsapp="888888888", papeis=[PapelUsuario.MOTORISTA])

@pytest.fixture
def corrida(motorista):
    cliente = Usuario(cpf="12345678900", nome="Cliente Teste", telefone_whatsapp="999999999", papeis=[PapelUsuario.CLIENTE])
    origem = Endereco("Rua A", "100", "Centro", "Cidade", "UF", "00000-000", -10.0, -20.0)
    destino = Endereco("Rua B", "200", "Bairro", "Cidade", "UF", "11111-111", -11.0, -21.0)
    return Corrida(
        id="c2",
        cliente=cliente,
        motorista=None,
        origem=origem,
        destino=destino,
        status=StatusCorrida.DESPACHADA
    )

def test_recusar_corrida(corrida, motorista):
    repo = FakeCorridaRepo(corrida)
    usecase = RecusarCorridaUseCase(repo)
    result = usecase.execute("c2", motorista, motivo="Não disponível")
    assert result.status == StatusCorrida.CANCELADA_MOTORISTA
    assert result.motorista.cpf == "11122233344"
    assert result.motivo_cancelamento == "Não disponível"
    assert repo.saved[0] == result
