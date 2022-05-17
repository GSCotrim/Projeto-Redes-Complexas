import sympy as sp
from Sistema import *
from Reservatorio import *


## LOCAL DE INTERAÇÃO PARA DEFINIR O SISTEMA QUE DESEJA-SE RESOLVER

def definindo_sistema():
    ## RESERVATÓRIOS
    res_A = Reservatorio("A", 10)
    res_C = Reservatorio("C", 30)
    res_D = Reservatorio("D", 15)

    ## NOS
    altura_B = sp.symbols('x[3]')
    no_B = Nos("B", altura_B, 1.42 * 10 ** -2)

    ## DUTOS
    vazao_1 = sp.symbols('x[0]')
    vazao_2 = sp.symbols('x[1]')
    vazao_3 = sp.symbols('x[2]')
    duto_AB = Duto(res_A, no_B, vazao_1, 0, 0, 50, 0.15, 0.02, 2)
    duto_BC = Duto(no_B, res_C, vazao_2, 0, 0, 100, 0.10, 0.015, 1)
    duto_BD = Duto(no_B, res_D, vazao_3, 0, 0, 300, 0.10, 0.025, 1)

    ## SISTEMA
    sistema = Sistema([duto_AB, duto_BC, duto_BD], [res_A, no_B, res_C, res_D])

    return sistema
