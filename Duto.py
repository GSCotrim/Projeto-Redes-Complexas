from math import pi


class Duto(object):

    def __init__(self, no_inicial, no_final, vazao, resistencia_predet, comprimento=0, diametro=0, fator_friccao=0,
                 coef_perdas_singulares=0, valor_bomba=0):
        self.no_inicial = no_inicial
        self.no_final = no_final
        self.vazao = vazao
        self.resistencia_predet = resistencia_predet
        self.comprimento = comprimento
        self.diametro = diametro
        self.fator_friccao = fator_friccao
        self.coef_perdas_singulares = coef_perdas_singulares
        self.valor_bomba = valor_bomba
        self.resistencia_hidraulica = self.calculadora_de_resistencia_hidraulica()

    def __str__(self):
        return f'({self.no_inicial}{self.no_final})'

    def __repr__(self):
        return self.__str__()

    def calculadora_de_resistencia_hidraulica(self):
        f = self.fator_friccao
        k = self.coef_perdas_singulares
        D = self.diametro
        L = self.comprimento

        if f and k == 0 and self.resistencia_predet != 0:
            resistencia = self.resistencia_predet

        else:
            resistencia = (8 * f * L) / (pi ** 2 * 9.81 * D ** 5) + (8 * k) / (pi ** 2 * 9.81 * D ** 4)

        return resistencia
