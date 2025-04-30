class EstatisticaMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Estatistica(metaclass=EstatisticaMeta):
    def __init__(self):
        self.__vitorias = 0
        self.__derrotas = 0
        self.__empates = 0

    def atualizar(self, resultado_jogada):
        if resultado_jogada == 'vitoria':
            self.__vitorias += 1
        elif resultado_jogada == 'derrota':
            self.__derrotas += 1
        else:
            self.__empates += 1

    def get_vitorias(self):
        return self.__vitorias

    def get_derrotas(self):
        return self.__derrotas

    def get_empates(self):
        return self.__empates