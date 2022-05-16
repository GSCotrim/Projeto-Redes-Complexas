import unittest
import numpy.testing
import sympy as sp
from Sistema import *
from Reservatorio import *
from Solver import *
import logging


class TestEverythingInOneSingleFile(unittest.TestCase):
    tolrancia = 10 ** -7

    def test_exemplo_11_5_Potter_SEM_BOMBA(self):
        # GIVEN
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
            duto_AB = Duto(res_A, no_B, vazao_1, 0, 50, 0.15, 0.02, 2)
            duto_BC = Duto(no_B, res_C, vazao_2, 0, 100, 0.10, 0.015, 1)
            duto_BD = Duto(no_B, res_D, vazao_3, 0, 300, 0.10, 0.025, 1)

            ## SISTEMA
            sistema = Sistema([duto_AB, duto_BC, duto_BD], [res_A, no_B, res_C, res_D])

            return sistema

        # WHEN
        sistema = definindo_sistema()
        eq = sistema.sistema_de_equacoes()
        solver = Solver(eq)
        func = solver.func()
        root = solver.solve_system(func)[0]
        solve = solver.solve_system(func)[1]
        size = len(eq)
        zeros = np.zeros(size)

        # THEN
        self.assertTrue(numpy.allclose(solve(root), zeros, atol=self.tolrancia))

    def test_exemplo_11_5_Potter_COM_BOMBA(self):
        # GIVEN
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
            duto_AB = Duto(res_A, no_B, vazao_1, 0, 50, 0.15, 0.02, 2, (2 * 10 ** 4) / (9800 * vazao_1))
            duto_BC = Duto(no_B, res_C, vazao_2, 0, 100, 0.10, 0.015, 1)
            duto_BD = Duto(no_B, res_D, vazao_3, 0, 300, 0.10, 0.025, 1)

            ## SISTEMA
            sistema = Sistema([duto_AB, duto_BC, duto_BD], [res_A, no_B, res_C, res_D])

            return sistema

        # WHEN
        sistema = definindo_sistema()
        eq = sistema.sistema_de_equacoes()
        solver = Solver(eq)
        func = solver.func()
        root = solver.solve_system(func)[0]
        solve = solver.solve_system(func)[1]
        size = len(eq)
        zeros = np.zeros(size)

        # THEN
        self.assertTrue(numpy.allclose(solve(root), zeros, atol=self.tolrancia))

    def test_exemplo_11_5_Potter_COM_BOMBA_VAZAO_PONTUAL_NO_DIF_0(self):
        # GIVEN
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
            duto_AB = Duto(res_A, no_B, vazao_1, 0, 50, 0.15, 0.02, 2, (2 * 10 ** 4) / (9800 * vazao_1))
            duto_BC = Duto(no_B, res_C, vazao_2, 0, 100, 0.10, 0.015, 1)
            duto_BD = Duto(no_B, res_D, vazao_3, 0, 300, 0.10, 0.025, 1)

            ## SISTEMA
            sistema = Sistema([duto_AB, duto_BC, duto_BD], [res_A, no_B, res_C, res_D])

            return sistema

        # WHEN
        sistema = definindo_sistema()
        eq = sistema.sistema_de_equacoes()
        solver = Solver(eq)
        func = solver.func()
        root = solver.solve_system(func)[0]
        solve = solver.solve_system(func)[1]
        size = len(eq)
        zeros = np.zeros(size)

        # THEN
        self.assertTrue(numpy.allclose(solve(root), zeros, atol=self.tolrancia))

    def test_exemplo_11_6_Potter(self):
        # GIVEN
        def definindo_sistema():
            ## RESERVATÓRIOS
            res_A = Reservatorio("A", 50)
            res_B = Reservatorio("B", 30)

            # NOS
            altura_C = sp.symbols('x[0]')
            altura_D = sp.symbols('x[1]')
            altura_E = sp.symbols('x[2]')
            altura_F = sp.symbols('x[3]')
            altura_G = sp.symbols('x[4]')

            no_C = Nos("C", altura_C)
            no_D = Nos("D", altura_D)
            no_E = Nos("E", altura_E)
            no_F = Nos("F", altura_F, 0.15)
            no_G = Nos("G", altura_G, 0.15)

            ## DUTOS
            vazao_1 = sp.symbols('x[5]')
            vazao_2 = sp.symbols('x[6]')
            vazao_3 = sp.symbols('x[7]')
            vazao_4 = sp.symbols('x[8]')
            vazao_5 = sp.symbols('x[9]')
            vazao_6 = sp.symbols('x[10]')
            vazao_7 = sp.symbols('x[11]')
            vazao_8 = sp.symbols('x[12]')

            duto_AC = Duto(res_A, no_C, vazao_1, 100)
            duto_CD = Duto(no_C, no_D, vazao_2, 500)
            duto_DE = Duto(no_D, no_E, vazao_3, 200)
            duto_EB = Duto(no_E, res_B, vazao_4, 100)
            duto_EG = Duto(no_E, no_G, vazao_5, 400)
            duto_CF = Duto(no_C, no_D, vazao_6, 300)
            duto_GF = Duto(no_G, no_F, vazao_7, 400)
            duto_GD = Duto(no_G, no_D, vazao_8, 300)

            ## SISTEMA
            sistema = Sistema([duto_AC, duto_CD, duto_DE, duto_EB, duto_EG, duto_CF, duto_GF, duto_GD],
                              [res_A, res_B, no_C, no_D, no_E, no_F, no_G])

            return sistema

        # WHEN
        sistema = definindo_sistema()
        eq = sistema.sistema_de_equacoes()
        solver = Solver(eq)
        func = solver.func()
        root = solver.solve_system(func)[0]
        solve = solver.solve_system(func)[1]
        size = len(eq)
        zeros = np.zeros(size)

        # THEN
        print(eq)
        self.assertTrue(numpy.allclose(solve(root), zeros, atol=self.tolrancia))


if __name__ == '__main__':
    unittest.main(verbosity=2)
