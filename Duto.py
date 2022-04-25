from Nos import *


class Duto(object):

    def __init__(self, no_inicial, no_final, vazao, resistencia_hidraulica, valor_bomba=0):
        self.no_inicial = no_inicial
        self.no_final = no_final
        self.vazao = vazao
        self.valor_bomba = valor_bomba
        self.resistencia_hidraulica = resistencia_hidraulica  # Talvez tenhamos que calcular essa propriedade no futuro

    def __str__(self):
        return f'({self.no_inicial}{self.no_final})'

    def __repr__(self):
        return self.__str__()

