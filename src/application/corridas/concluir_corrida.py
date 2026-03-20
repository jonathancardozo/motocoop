from src.domain.corridas.entities import Corrida, StatusCorrida
from src.domain.corridas.repositories import ICorridaRepository

class ConcluirCorridaUseCase:
    def __init__(self, corrida_repo: ICorridaRepository):
        self.corrida_repo = corrida_repo

    def execute(self, corrida_id: str) -> Corrida:
        corrida = self.corrida_repo.get_by_id(corrida_id)
        if corrida.status != StatusCorrida.EM_ANDAMENTO:
            raise Exception("Corrida não está em andamento.")
        corrida.status = StatusCorrida.CONCLUIDA
        corrida.conclusao_ts = "auto"  # timestamp atual
        self.corrida_repo.save(corrida)
        return corrida
