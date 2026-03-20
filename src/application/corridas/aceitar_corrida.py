from src.domain.corridas.entities import Corrida, StatusCorrida
from src.domain.usuarios.entities import Usuario
from src.domain.corridas.repositories import ICorridaRepository

class AceitarCorridaUseCase:
    def __init__(self, corrida_repo: ICorridaRepository):
        self.corrida_repo = corrida_repo

    def execute(self, corrida_id: str, motorista: Usuario) -> Corrida:
        corrida = self.corrida_repo.get_by_id(corrida_id)
        if corrida.status != StatusCorrida.DESPACHADA:
            raise Exception("Corrida não está disponível para aceitação.")
        corrida.motorista = motorista
        corrida.status = StatusCorrida.ACEITA
        corrida.inicio_ts = "auto"  # timestamp atual
        self.corrida_repo.save(corrida)
        return corrida
