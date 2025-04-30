from random import randint


def jogar_pedra_papel_tesoura(jogada: int):
    jogada_pc = randint(1, 3)

    if jogada == jogada_pc:
        return 'empate'
    elif ((jogada == 1 and jogada_pc == 3)
          or (jogada == 2 and jogada_pc == 1)
          or (jogada == 3 and jogada_pc == 2)):
        return 'vitoria'
    else:
        return 'derrota'