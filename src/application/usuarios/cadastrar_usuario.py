from src.domain.usuarios.entities import Usuario, PapelUsuario
from src.domain.usuarios.repositories import IUsuarioRepository
from typing import List, Optional

class CadastrarUsuarioUseCase:
    def __init__(self, usuario_repo: IUsuarioRepository):
        self.usuario_repo = usuario_repo

    def execute(
        self,
        cpf: str,
        nome: str,
        telefone_whatsapp: str,
        papeis: List[PapelUsuario],
        veiculo: Optional[str] = None,
        central_id: Optional[str] = None
    ) -> Usuario:
        usuario = Usuario(
            cpf=cpf,
            nome=nome,
            telefone_whatsapp=telefone_whatsapp,
            papeis=papeis,
            veiculo=veiculo,
            central_id=central_id
        )
        self.usuario_repo.save(usuario)
        return usuario
