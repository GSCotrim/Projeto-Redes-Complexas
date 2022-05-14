import unittest
import numpy.testing
import sympy as sp
from Sistema import *
from Reservatorio import *
from Solver import *


class TestEverythingInOneSingleFile(unittest.TestCase):
    tolrancia = 10 ** -7

    def test_exemplo_11_5_Potter_SEM_BOMBA(self):
        # GIVEN
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
            ## NOS
            res_A = Reservatorio("A", 10)
            altura_B = sp.symbols('x[3]')
            no_B = Nos("B", altura_B, 1.42 * 10 ** -2)
            res_C = Reservatorio("C", 30)
            res_D = Reservatorio("D", 15)

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

    
if __name__ == '__main__':
    unittest.main(verbosity=2)
