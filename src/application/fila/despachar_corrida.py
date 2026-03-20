from src.domain.corridas.entities import Corrida, StatusCorrida
from src.domain.usuarios.entities import Usuario
from src.domain.corridas.repositories import ICorridaRepository
from .gerenciar_fila import FilaMotoristas

class DespacharCorridaUseCase:
    def __init__(self, corrida_repo: ICorridaRepository, fila_motoristas: FilaMotoristas):
        self.corrida_repo = corrida_repo
        self.fila_motoristas = fila_motoristas

    def execute(self, corrida_id: str) -> Corrida:
        corrida = self.corrida_repo.get_by_id(corrida_id)
        if corrida.status != StatusCorrida.SOLICITADA:
            raise Exception("Corrida não está pronta para despacho.")
        proximo_cpf = self.fila_motoristas.proximo_motorista()
        if not proximo_cpf:
            raise Exception("Nenhum motorista disponível na fila.")
        # O vínculo do motorista será feito na aceitação
        corrida.status = StatusCorrida.DESPACHADA
        self.corrida_repo.save(corrida)
        return corrida
