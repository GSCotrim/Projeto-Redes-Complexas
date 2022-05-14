import sympy as sp
from Sistema import *
from Reservatorio import *


## LOCAL DE INTERAÇÃO PARA DEFINIR O SISTEMA QUE DESEJA-SE RESOLVER

def definindo_sistema():
    ## NOS
    res_A = Reservatorio("A", 10)
    altura_B = sp.symbols('x[3]')
    no_B = Nos("B", altura_B)
    res_C = Reservatorio("C", 30)
    res_D = Reservatorio("D", 15)

    ## DUTOS
    vazao_1 = sp.symbols('x[0]')
    vazao_2 = sp.symbols('x[1]')
    vazao_3 = sp.symbols('x[2]')
    duto_AB = Duto(res_A, no_B, vazao_1, 50, 0.15, 0.02, 2, (2 * 10 ** 4) / (9800 * vazao_1))
    duto_BC = Duto(no_B, res_C, vazao_2, 100, 0.10, 0.015, 1)
    duto_BD = Duto(no_B, res_D, vazao_3, 300, 0.10, 0.025, 1)

    ## SISTEMA
    sistema = Sistema([duto_AB, duto_BC, duto_BD], [res_A, no_B, res_C, res_D])

    return sistema
