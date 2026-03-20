from src.domain.centrais.entities import Central
from src.domain.centrais.repositories import ICentralRepository
from typing import List

class CadastrarCentralUseCase:
    def __init__(self, central_repo: ICentralRepository):
        self.central_repo = central_repo

    def execute(
        self,
        id: str,
        nome: str,
        area_cobertura: object,
        administradores: List[str]
    ) -> Central:
        central = Central(
            id=id,
            nome=nome,
            area_cobertura=area_cobertura,
            administradores=administradores
        )
        self.central_repo.save(central)
        return central
