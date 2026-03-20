from enum import Enum
from typing import Optional, List

class PapelUsuario(Enum):
    CLIENTE = "cliente"
    MOTORISTA = "motorista"
    ADMINISTRADOR = "administrador"

class Usuario:
    def __init__(
        self,
        cpf: str,
        nome: str,
        telefone_whatsapp: str,
        papeis: List[PapelUsuario],
        veiculo: Optional[str] = None,
        central_id: Optional[str] = None
    ):
        self.cpf = cpf
        self.nome = nome
        self.telefone_whatsapp = telefone_whatsapp
        self.papeis = papeis
        self.veiculo = veiculo  # Só para motoristas
        self.central_id = central_id  # Só para motoristas/administradores

    def is_motorista(self) -> bool:
        return PapelUsuario.MOTORISTA in self.papeis

    def is_cliente(self) -> bool:
        return PapelUsuario.CLIENTE in self.papeis

    def is_administrador(self) -> bool:
        return PapelUsuario.ADMINISTRADOR in self.papeis
