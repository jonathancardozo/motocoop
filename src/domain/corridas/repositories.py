from abc import ABC, abstractmethod
from .entities import Corrida

class ICorridaRepository(ABC):
    @abstractmethod
    def get_by_id(self, id: str) -> Corrida:
        pass

    @abstractmethod
    def save(self, corrida: Corrida) -> None:
        pass

    @abstractmethod
    def list_by_status(self, status: str) -> list[Corrida]:
        pass
