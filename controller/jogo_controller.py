from model.estatistica import Estatistica
from model.pedra_papel_tesoura import jogar_pedra_papel_tesoura

def realizar_jogada(jogada: int):
    resultado = jogar_pedra_papel_tesoura(jogada)
    Estatistica().atualizar(resultado)
    return resultado