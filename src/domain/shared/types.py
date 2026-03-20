from enum import Enum

class StatusMotorista(Enum):
    ATIVO = "ativo"
    EM_CORRIDA = "em_corrida"
    PAUSA = "pausa"
    INATIVO = "inativo"

class Veiculo:
    def __init__(self, placa: str, modelo: str, cor: str):
        self.placa = placa
        self.modelo = modelo
        self.cor = cor
