from src.application.fila.gerenciar_fila import FilaMotoristas
from src.domain.usuarios.entities import Usuario, PapelUsuario

def test_entrar_e_sair_fila():
    fila = FilaMotoristas()
    motorista = Usuario(cpf="11122233344", nome="Motorista Teste", telefone_whatsapp="888888888", papeis=[PapelUsuario.MOTORISTA])
    fila.entrar_fila(motorista)
    assert fila.listar_fila() == ["11122233344"]
    fila.sair_fila(motorista)
    assert fila.listar_fila() == []

def test_proximo_motorista():
    fila = FilaMotoristas()
    m1 = Usuario(cpf="11122233344", nome="M1", telefone_whatsapp="888888888", papeis=[PapelUsuario.MOTORISTA])
    m2 = Usuario(cpf="55566677788", nome="M2", telefone_whatsapp="777777777", papeis=[PapelUsuario.MOTORISTA])
    fila.entrar_fila(m1)
    fila.entrar_fila(m2)
    assert fila.proximo_motorista() == "11122233344"
    fila.sair_fila(m1)
    assert fila.proximo_motorista() == "55566677788"
