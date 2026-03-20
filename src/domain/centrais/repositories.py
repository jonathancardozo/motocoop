from abc import ABC, abstractmethod
from .entities import Central

class ICentralRepository(ABC):
    @abstractmethod
    def get_by_id(self, id: str) -> Central:
        pass

    @abstractmethod
    def save(self, central: Central) -> None:
        pass

    @abstractmethod
    def list_all(self) -> list[Central]:
        pass
