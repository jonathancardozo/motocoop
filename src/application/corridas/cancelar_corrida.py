from src.domain.corridas.entities import Corrida, StatusCorrida
from src.domain.corridas.repositories import ICorridaRepository

class CancelarCorridaUseCase:
    def __init__(self, corrida_repo: ICorridaRepository):
        self.corrida_repo = corrida_repo

    def execute(self, corrida_id: str, motivo: str = "Cancelada pelo cliente") -> Corrida:
        corrida = self.corrida_repo.get_by_id(corrida_id)
        if corrida.status not in [StatusCorrida.SOLICITADA, StatusCorrida.DESPACHADA]:
            raise Exception("Corrida não pode ser cancelada neste status.")
        corrida.status = StatusCorrida.CANCELADA_CLIENTE
        corrida.motivo_cancelamento = motivo
        self.corrida_repo.save(corrida)
        return corrida
