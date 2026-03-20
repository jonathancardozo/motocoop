import pytest
from src.application.corridas.solicitar_corrida import SolicitarCorridaUseCase
from src.domain.corridas.entities import StatusCorrida
from src.domain.usuarios.entities import Usuario, PapelUsuario
from src.domain.shared.value_objects import Endereco

class FakeCorridaRepo:
    def __init__(self):
        self.saved = []
    def save(self, corrida):
        self.saved.append(corrida)

@pytest.fixture
def corrida_repo():
    return FakeCorridaRepo()

@pytest.fixture
def cliente():
    return Usuario(cpf="12345678900", nome="Cliente Teste", telefone_whatsapp="999999999", papeis=[PapelUsuario.CLIENTE])

@pytest.fixture
def origem():
    return Endereco("Rua A", "100", "Centro", "Cidade", "UF", "00000-000", -10.0, -20.0)

@pytest.fixture
def destino():
    return Endereco("Rua B", "200", "Bairro", "Cidade", "UF", "11111-111", -11.0, -21.0)

def test_solicitar_corrida(corrida_repo, cliente, origem, destino):
    usecase = SolicitarCorridaUseCase(corrida_repo)
    corrida = usecase.execute(cliente, origem, destino, valor=10.0, forma_pagamento="dinheiro")
    assert corrida.status == StatusCorrida.SOLICITADA
    assert corrida.cliente.cpf == "12345678900"
    assert corrida_repo.saved[0] == corrida
