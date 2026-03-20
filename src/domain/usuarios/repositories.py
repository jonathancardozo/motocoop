from abc import ABC, abstractmethod
from .entities import Usuario

class IUsuarioRepository(ABC):
    @abstractmethod
    def get_by_cpf(self, cpf: str) -> Usuario:
        pass

    @abstractmethod
    def save(self, usuario: Usuario) -> None:
        pass

    @abstractmethod
    def list_by_papel(self, papel: str) -> list[Usuario]:
        pass
