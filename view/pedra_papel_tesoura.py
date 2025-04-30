from controller.jogo_controller import realizar_jogada


def jogar_pedra_papel_tesoura():
    print('*' * 50)
    print('PEDRA, PAPEL E TESOURA'.center(50))
    print('*' * 50)

    print('\nO computador já fez a escolha dele... agora é a sua vez!')

    print('\nFaça sua jogada:')
    print('[ 1 ] Pedra')
    print('[ 2 ] Papel')
    print('[ 3 ] Tesoura')

    print('\n[0] Voltar ao menu principal')

    escolha = int(input('\nDigite o número da sua escolha e pressione Enter: '))

    if escolha == 0:
        return
    else:
        resultado = realizar_jogada(escolha)
        if resultado == 'vitoria':
            mostrar_vitoria()
        elif resultado == 'derrota':
            mostrar_derrota()
        else:
            mostrar_empate()

def mostrar_vitoria():
    print('*' * 50)
    print('VOCÊ VENCEU!'.center(50))
    print('*' * 50)

    print('\nParabéns! Sua jogada foi imbatível!')

    print('\nQuer continuar sua série de vitórias?')
    print('[1] Jogar novamente')
    print('[0] Voltar ao menu principal')

    escolha = int(input('\nDigite o número da sua escolha e pressione Enter: '))
    if escolha == 1:
        jogar_pedra_papel_tesoura()

def mostrar_derrota():
    print('*' * 50)
    print('VOCÊ PERDEU!'.center(50))
    print('*' * 50)

    print('\nO computador levou essa, mas não desanime!')

    print('\nQuer uma revanche?')
    print('[1] Jogar novamente')
    print('[0] Voltar ao menu principal')

    escolha = int(input('\nDigite o número da sua escolha e pressione Enter: '))
    if escolha == 1:
        jogar_pedra_papel_tesoura()

def mostrar_empate():
    print('*' * 50)
    print('EMPATE!'.center(50))
    print('*' * 50)

    print('\nAmbos escolheram a mesma coisa! Que coincidência!')

    print('\nQuer tentar de novo?')
    print('[1] Jogar novamente')
    print('[0] Voltar ao menu principal')

    escolha = int(input('\nDigite o número da sua escolha e pressione Enter: '))
    if escolha == 1:
        jogar_pedra_papel_tesoura()