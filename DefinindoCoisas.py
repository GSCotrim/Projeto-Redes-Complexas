import sympy as sp
from Duto import *
from Nos import *
from Reservatorio import *
from Sistema import *


def definindo_sistema():
    ## NOS
    res_A = Reservatorio("A", 10, 0)
    altura_B = sp.symbols('altura_B')
    no_B = Nos("B", altura_B, 0)
    res_C = Reservatorio("C", 15, 0)
    res_D = Reservatorio("D", 30, 0)

    ## DUTOS
    vazao_1 = sp.symbols('vazao_1')
    vazao_2 = sp.symbols('vazao_2')
    vazao_3 = sp.symbols('vazao_3')
    duto_AB = Duto(res_A, no_B, vazao_1, 1.42 * 10 ** 3)
    duto_BC = Duto(no_B, res_C, vazao_2, 1.32 * 10 ** 4)
    duto_BD = Duto(no_B, res_D, vazao_3, 6.28 * 10 ** 4)

    ## SISTEMA
    sistema = Sistema([duto_AB, duto_BC, duto_BD], [res_A, no_B, res_C, res_D])

    ## SE QUISER UM GRAFO
    # sistema.grafo()

    ## Quero saber todos os dutos que passam no nó B
    sistema.give_reservatorios_please()
    sistema.give_nos_please()
    sistema.give_dutos_do_no_please(res_C)
    sistema.give_dutos_do_no_please(no_B)
    sistema.give_dutos_do_no_por_nome_please("D")
    sistema.sistema_de_equacoes()

    ## pra fazer as contas
    # sistema.give_dutos(NO)
    # for duto in dutos:

    return sistema
