from typing import List
from src.domain.usuarios.entities import Usuario, PapelUsuario

class FilaMotoristas:
    def __init__(self):
        self.fila: List[str] = []  # lista de CPFs

    def entrar_fila(self, motorista: Usuario):
        if motorista.cpf not in self.fila and motorista.is_motorista():
            self.fila.append(motorista.cpf)

    def sair_fila(self, motorista: Usuario):
        if motorista.cpf in self.fila:
            self.fila.remove(motorista.cpf)

    def proximo_motorista(self) -> str:
        return self.fila[0] if self.fila else None

    def listar_fila(self) -> List[str]:
        return self.fila.copy()
