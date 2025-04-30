from controller.estatistica_controller import obter_estatisticas


def visualizar_estatisticas():
    print('*' * 50)
    print('SUAS ESTATÍSTICAS'.center(50))
    print('*' * 50)

    estatisticas = obter_estatisticas()

    print(f'\nVitórias: {estatisticas.get_vitorias()}')
    print(f'Derrotas: {estatisticas.get_derrotas()}')
    print(f'Empates: {estatisticas.get_empates()}')

    print('\nContinue jogando e melhore seus resultados!')

    input('\nPressione Enter para voltar ao menu principal: ')
