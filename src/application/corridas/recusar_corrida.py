from src.domain.corridas.entities import Corrida, StatusCorrida
from src.domain.usuarios.entities import Usuario
from src.domain.corridas.repositories import ICorridaRepository

class RecusarCorridaUseCase:
    def __init__(self, corrida_repo: ICorridaRepository):
        self.corrida_repo = corrida_repo

    def execute(self, corrida_id: str, motorista: Usuario, motivo: str = "Recusada pelo motorista") -> Corrida:
        corrida = self.corrida_repo.get_by_id(corrida_id)
        if corrida.status != StatusCorrida.DESPACHADA:
            raise Exception("Corrida não está disponível para recusa.")
        corrida.motorista = motorista
        corrida.status = StatusCorrida.CANCELADA_MOTORISTA
        corrida.motivo_cancelamento = motivo
        self.corrida_repo.save(corrida)
        return corrida
