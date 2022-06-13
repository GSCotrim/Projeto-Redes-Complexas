from math import pi
import sympy as sp
import numpy as np
from Fluido import *


class Duto(object):

    def __init__(self, no_inicial, no_final, vazao, resistencia_predet, valor_bomba, comprimento=0, diametro=0,
                 fator_friccao=0, coef_perdas_singulares=0, rugosidade_absoluta=0):
        self.no_inicial = no_inicial
        self.no_final = no_final
        self.vazao = vazao
        self.resistencia_predet = resistencia_predet
        self.valor_bomba = valor_bomba
        self.rugosidade_absoluta = rugosidade_absoluta
        self.comprimento = comprimento
        self.diametro = diametro
        self.coef_perdas_singulares = coef_perdas_singulares
        self.area_seccao = pi * (self.diametro / 2) ** 2

        # ESSES IF'S ESTÃO ME INCOMODANDO MUITO
        if diametro != 0:
            self.rugosidade_relativa = self.rugosidade_absoluta / self.diametro

        if fator_friccao == 0 and diametro != 0:
            self.fator_friccao = self.calculadora_fator_friccao()
        else:
            self.fator_friccao = fator_friccao

        self.resistencia_hidraulica = self.calculadora_de_resistencia_hidraulica()

    def __str__(self):
        return f'({self.no_inicial}{self.no_final})'

    def __repr__(self):
        return self.__str__()

    agua_20_graus = Fluido(0.9982, 1.002 * 10 ** -3)  # (kg/L, N.s/m², ) -- NÃO GOSTEI DISSO CHUMBADO AQUI.

    def reynolds(self):
        Q = self.vazao
        A = self.area_seccao
        D = self.diametro
        densidade_fluido = self.agua_20_graus.densidade
        viscosidade_dinamica_fluido = self.agua_20_graus.viscosidade_dinamica

        Re = (densidade_fluido * (Q / A) * D) / viscosidade_dinamica_fluido

        return np.abs(Re)

    def calculadora_fator_friccao(self):
        Re = self.reynolds()
        # Re = 10 ** 6
        rug_rel = self.rugosidade_relativa

        # O LOG DO SYMPY É LOG NATURAL, NÃO É LOG10 -- NA CLASSE SOLVE "CORRIGIMOS" PARA LOG BASE 10
        # fator_friccao = ((-2 * sp.log((rug_rel / 3.7065) - (5.0272 / Re) * sp.log(
        #     (rug_rel / 3.827) - (4.567 / Re) * sp.log(
        #         ((rug_rel / 7.7918) ** 0.9924) + (5.3326 / (208.815 + Re) ** 0.9345))))) ** 2) ** -1

        # FATOR DE FRICÇÃO HAALAND
        fator_friccao = 1.0 / (-1.8 * sp.log((rug_rel / 3.7) ** 1.11 + 6.9 / Re)) ** 2

        return fator_friccao

    def calculadora_de_resistencia_hidraulica(self):
        f = self.fator_friccao
        k = self.coef_perdas_singulares
        D = self.diametro
        L = self.comprimento

        if f == 0 and k == 0 and self.resistencia_predet != 0:
            resistencia = self.resistencia_predet

        else:
            resistencia = (8 * f * L) / (pi ** 2 * 9.81 * D ** 5) + (8 * k) / (pi ** 2 * 9.81 * D ** 4)

        return resistencia
