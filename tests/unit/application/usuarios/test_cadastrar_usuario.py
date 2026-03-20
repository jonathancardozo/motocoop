from src.application.usuarios.cadastrar_usuario import CadastrarUsuarioUseCase
from src.domain.usuarios.entities import PapelUsuario

class FakeUsuarioRepo:
    def __init__(self):
        self.saved = []
    def save(self, usuario):
        self.saved.append(usuario)

def test_cadastrar_usuario():
    repo = FakeUsuarioRepo()
    usecase = CadastrarUsuarioUseCase(repo)
    usuario = usecase.execute(
        cpf="12345678900",
        nome="Cliente Teste",
        telefone_whatsapp="999999999",
        papeis=[PapelUsuario.CLIENTE]
    )
    assert usuario.cpf == "12345678900"
    assert PapelUsuario.CLIENTE in usuario.papeis
    assert repo.saved[0] == usuario
