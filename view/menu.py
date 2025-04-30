from view.estatistica import visualizar_estatisticas
from view.pedra_papel_tesoura import jogar_pedra_papel_tesoura

def mostrar_menu():
    while True:
        print('*' * 50)
        print('TERMINAL GAMES'.center(50))
        print('*' * 50)

        print('Sua central de diversão diretamente no terminal!')
        print('Escolha um jogo para começar:')

        print('\n[ 1 ] Estatísticas')
        print('[ 2 ] Pedra, Papel e Tesoura')
        print('\n[ 0 ] Sair')

        escolha_jogador = int(input('\nDigite o número da sua escolha e pressione Enter: '))

        if escolha_jogador == 0:
            break
        elif escolha_jogador == 1:
            mostrar_estatisticas()
        else:
            mostrar_jogo()

def mostrar_estatisticas():
    visualizar_estatisticas()

def mostrar_jogo():
    jogar_pedra_papel_tesoura()
