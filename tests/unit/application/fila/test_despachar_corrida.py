import pytest
from src.application.fila.despachar_corrida import DespacharCorridaUseCase
from src.domain.corridas.entities import Corrida, StatusCorrida
from src.domain.usuarios.entities import Usuario, PapelUsuario
from src.domain.shared.value_objects import Endereco
from src.application.fila.gerenciar_fila import FilaMotoristas

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
        id="c5",
        cliente=cliente,
        motorista=None,
        origem=origem,
        destino=destino,
        status=StatusCorrida.SOLICITADA
    )

def test_despachar_corrida(corrida):
    repo = FakeCorridaRepo(corrida)
    fila = FilaMotoristas()
    m1 = Usuario(cpf="11122233344", nome="M1", telefone_whatsapp="888888888", papeis=[PapelUsuario.MOTORISTA])
    fila.entrar_fila(m1)
    usecase = DespacharCorridaUseCase(repo, fila)
    result = usecase.execute("c5")
    assert result.status == StatusCorrida.DESPACHADA
    assert repo.saved[0] == result
