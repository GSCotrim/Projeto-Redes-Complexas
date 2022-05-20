import unittest
import numpy.testing
import sympy as sp
from Sistema import *
from Reservatorio import *
from Solver import *
import logging


class TestEverythingInOneSingleFile(unittest.TestCase):
    tolerancia = 10 ** -7

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
            duto_AB = Duto(res_A, no_B, vazao_1, 0, 0, 50, 0.15, 0.02, 2)
            duto_BC = Duto(no_B, res_C, vazao_2, 0, 0, 100, 0.10, 0.015, 1)
            duto_BD = Duto(no_B, res_D, vazao_3, 0, 0, 300, 0.10, 0.025, 1)

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
        self.assertTrue(numpy.allclose(solve(root), zeros, atol=self.tolerancia))

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
            duto_AB = Duto(res_A, no_B, vazao_1, 0, (2 * 10 ** 4) / (9800 * vazao_1), 50, 0.15, 0.02, 2)
            duto_BC = Duto(no_B, res_C, vazao_2, 0, 0, 100, 0.10, 0.015, 1)
            duto_BD = Duto(no_B, res_D, vazao_3, 0, 0, 300, 0.10, 0.025, 1)

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
        self.assertTrue(numpy.allclose(solve(root), zeros, atol=self.tolerancia))

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

            duto_AB = Duto(res_A, no_B, vazao_1, 0, (2 * 10 ** 4) / (9800 * vazao_1), 50, 0.15, 0.02, 2)
            duto_BC = Duto(no_B, res_C, vazao_2, 0, 0, 100, 0.10, 0.015, 1)
            duto_BD = Duto(no_B, res_D, vazao_3, 0, 0, 300, 0.10, 0.025, 1)

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
        self.assertTrue(numpy.allclose(solve(root), zeros, atol=self.tolerancia))

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

            duto_AC = Duto(res_A, no_C, vazao_1, 100, 0)
            duto_CD = Duto(no_C, no_D, vazao_2, 500, 0)
            duto_DE = Duto(no_D, no_E, vazao_3, 200, 0)
            duto_EB = Duto(no_E, res_B, vazao_4, 100, 0)
            duto_EG = Duto(no_E, no_G, vazao_5, 400, 0)
            duto_CF = Duto(no_C, no_F, vazao_6, 300, 0)
            duto_GF = Duto(no_G, no_F, vazao_7, 400, 0)
            duto_GD = Duto(no_G, no_D, vazao_8, 300, 0)

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
        self.assertTrue(numpy.allclose(solve(root), zeros, atol=self.tolerancia))

    def test_trabalho_oficial_fator_friccao_FIXO(self):
        # GIVEN
        fator_friccao = 0.02
        perdas_singulares = 2

        def definindo_sistema():
            ## RESERVATÓRIOS
            res_A = Reservatorio("A", 0)
            res_B = Reservatorio("B", 45.72)

            # NOS
            altura_C = sp.symbols('x[0]')
            altura_D = sp.symbols('x[1]')
            altura_E = sp.symbols('x[2]')
            altura_F = sp.symbols('x[3]')
            altura_G = sp.symbols('x[4]')
            altura_H = sp.symbols('x[5]')
            altura_I = sp.symbols('x[6]')
            altura_J = sp.symbols('x[7]')
            altura_K = sp.symbols('x[8]')

            no_C = Nos("C", altura_C)
            no_D = Nos("D", altura_D, 0.0142)
            no_E = Nos("E", altura_E)
            no_F = Nos("F", altura_F, 0.0142)
            no_G = Nos("G", altura_G, -0.0425)
            no_H = Nos("H", altura_H, 0.0142)
            no_I = Nos("I", altura_I, 0.0283)
            no_J = Nos("J", altura_J, 0.0566)
            no_K = Nos("K", altura_K, 0.0566)

            ## DUTOS
            vazao_1 = sp.symbols('x[9]')
            vazao_2 = sp.symbols('x[10]')
            vazao_3 = sp.symbols('x[11]')
            vazao_4 = sp.symbols('x[12]')
            vazao_5 = sp.symbols('x[13]')
            vazao_6 = sp.symbols('x[14]')
            vazao_7 = sp.symbols('x[15]')
            vazao_8 = sp.symbols('x[16]')
            vazao_9 = sp.symbols('x[17]')
            vazao_10 = sp.symbols('x[18]')
            vazao_11 = sp.symbols('x[19]')
            vazao_12 = sp.symbols('x[20]')
            vazao_13 = sp.symbols('x[21]')
            vazao_14 = sp.symbols('x[22]')
            vazao_15 = sp.symbols('x[23]')
            vazao_16 = sp.symbols('x[24]')

            duto_AC = Duto(res_A, no_C, vazao_1, 0, -8.2185 * vazao_1 ** 2 + 16.707 * vazao_1 + 47.332, 304.8, 0.3048,
                           fator_friccao, perdas_singulares)
            duto_CD = Duto(no_C, no_D, vazao_2, 0, 0, 304.8, 0.2032, fator_friccao, perdas_singulares)
            duto_DE = Duto(no_D, no_E, vazao_3, 0, 0, 304.8, 0.2032, fator_friccao, perdas_singulares)
            duto_EB = Duto(no_E, res_B, vazao_4, 0, 0, 152.4, 0.3048, fator_friccao, perdas_singulares)
            duto_EF = Duto(no_E, no_F, vazao_5, 0, 0, 396.24, 0.2032, fator_friccao, perdas_singulares)
            duto_FJ = Duto(no_F, no_J, vazao_6, 0, 0, 487.68, 0.254, fator_friccao, perdas_singulares)
            duto_JK = Duto(no_J, no_K, vazao_7, 0, 0, 304.8, 0.254, fator_friccao, perdas_singulares)
            duto_KI = Duto(no_K, no_I, vazao_8, 0, 0, 396.24, 0.254, fator_friccao, perdas_singulares)
            duto_IH = Duto(no_I, no_H, vazao_9, 0, 0, 274.32, 0.3048, fator_friccao, perdas_singulares)
            duto_HG = Duto(no_H, no_G, vazao_10, 0, 0, 274.32, 0.254, fator_friccao, perdas_singulares)
            duto_CG = Duto(no_C, no_G, vazao_11, 0, 0, 304.8, 0.254, fator_friccao, perdas_singulares)
            duto_DH = Duto(no_D, no_H, vazao_12, 0, 0, 365.76, 0.254, fator_friccao, perdas_singulares)
            duto_DI = Duto(no_D, no_I, vazao_13, 0, 0, 457.2, 0.254, fator_friccao, perdas_singulares)
            duto_EI = Duto(no_E, no_I, vazao_14, 0, 0, 426.72, 0.254, fator_friccao, perdas_singulares)
            duto_EJ = Duto(no_E, no_J, vazao_15, 0, 0, 609.6, 0.3048, fator_friccao, perdas_singulares)
            duto_JI = Duto(no_J, no_I, vazao_16, 0, 0, 365.76, 0.2032, fator_friccao, perdas_singulares)

            ## SISTEMA
            sistema = Sistema(
                [duto_AC, duto_CD, duto_DE, duto_EB, duto_EF, duto_FJ, duto_JK, duto_KI, duto_IH, duto_HG, duto_CG,
                 duto_DH, duto_DI, duto_EI, duto_EJ, duto_JI],
                [res_A, res_B, no_C, no_D, no_E, no_F, no_G, no_H, no_I, no_J, no_K])

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
        self.assertTrue(numpy.allclose(solve(root), zeros, atol=self.tolerancia))

    def test_trabalho_oficial_fator_friccao_CALCULADO(self):
        # GIVEN
        perdas_singulares = 2

        def definindo_sistema():
            ## RESERVATÓRIOS
            res_A = Reservatorio("A", 0)
            res_B = Reservatorio("B", 45.72)

            # NOS
            altura_C = sp.symbols('x[0]')
            altura_D = sp.symbols('x[1]')
            altura_E = sp.symbols('x[2]')
            altura_F = sp.symbols('x[3]')
            altura_G = sp.symbols('x[4]')
            altura_H = sp.symbols('x[5]')
            altura_I = sp.symbols('x[6]')
            altura_J = sp.symbols('x[7]')
            altura_K = sp.symbols('x[8]')

            no_C = Nos("C", altura_C)
            no_D = Nos("D", altura_D, 0.0142)
            no_E = Nos("E", altura_E)
            no_F = Nos("F", altura_F, 0.0142)
            no_G = Nos("G", altura_G, -0.0425)
            no_H = Nos("H", altura_H, 0.0142)
            no_I = Nos("I", altura_I, 0.0283)
            no_J = Nos("J", altura_J, 0.0566)
            no_K = Nos("K", altura_K, 0.0566)

            ## DUTOS
            vazao_1 = sp.symbols('x[9]')
            vazao_2 = sp.symbols('x[10]')
            vazao_3 = sp.symbols('x[11]')
            vazao_4 = sp.symbols('x[12]')
            vazao_5 = sp.symbols('x[13]')
            vazao_6 = sp.symbols('x[14]')
            vazao_7 = sp.symbols('x[15]')
            vazao_8 = sp.symbols('x[16]')
            vazao_9 = sp.symbols('x[17]')
            vazao_10 = sp.symbols('x[18]')
            vazao_11 = sp.symbols('x[19]')
            vazao_12 = sp.symbols('x[20]')
            vazao_13 = sp.symbols('x[21]')
            vazao_14 = sp.symbols('x[22]')
            vazao_15 = sp.symbols('x[23]')
            vazao_16 = sp.symbols('x[24]')

            duto_AC = Duto(res_A, no_C, vazao_1, 0, -8.2185 * vazao_1 ** 2 + 16.707 * vazao_1 + 47.332, 304.8, 0.3048,
                           0, perdas_singulares, 0.26)
            duto_CD = Duto(no_C, no_D, vazao_2, 0, 0, 304.8, 0.2032, 0, perdas_singulares, 0.26)
            duto_DE = Duto(no_D, no_E, vazao_3, 0, 0, 304.8, 0.2032, 0, perdas_singulares, 0.26)
            duto_EB = Duto(no_E, res_B, vazao_4, 0, 0, 152.4, 0.3048, 0, perdas_singulares, 0.26)
            duto_EF = Duto(no_E, no_F, vazao_5, 0, 0, 396.24, 0.2032, 0, perdas_singulares, 0.26)
            duto_FJ = Duto(no_F, no_J, vazao_6, 0, 0, 487.68, 0.254, 0, perdas_singulares, 0.26)
            duto_JK = Duto(no_J, no_K, vazao_7, 0, 0, 304.8, 0.254, 0, perdas_singulares, 0.26)
            duto_KI = Duto(no_K, no_I, vazao_8, 0, 0, 396.24, 0.254, 0, perdas_singulares, 0.26)
            duto_IH = Duto(no_I, no_H, vazao_9, 0, 0, 274.32, 0.3048, 0, perdas_singulares, 0.26)
            duto_HG = Duto(no_H, no_G, vazao_10, 0, 0, 274.32, 0.254, 0, perdas_singulares, 0.26)
            duto_CG = Duto(no_C, no_G, vazao_11, 0, 0, 304.8, 0.254, 0, perdas_singulares, 0.26)
            duto_DH = Duto(no_D, no_H, vazao_12, 0, 0, 365.76, 0.254, 0, perdas_singulares, 0.26)
            duto_DI = Duto(no_D, no_I, vazao_13, 0, 0, 457.2, 0.254, 0, perdas_singulares, 0.26)
            duto_EI = Duto(no_E, no_I, vazao_14, 0, 0, 426.72, 0.254, 0, perdas_singulares, 0.26)
            duto_EJ = Duto(no_E, no_J, vazao_15, 0, 0, 609.6, 0.3048, 0, perdas_singulares, 0.26)
            duto_JI = Duto(no_J, no_I, vazao_16, 0, 0, 365.76, 0.2032, 0, perdas_singulares, 0.26)

            ## SISTEMA
            sistema = Sistema(
                [duto_AC, duto_CD, duto_DE, duto_EB, duto_EF, duto_FJ, duto_JK, duto_KI, duto_IH, duto_HG, duto_CG,
                 duto_DH, duto_DI, duto_EI, duto_EJ, duto_JI],
                [res_A, res_B, no_C, no_D, no_E, no_F, no_G, no_H, no_I, no_J, no_K])

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
        self.assertTrue(numpy.allclose(solve(root), zeros, atol=self.tolerancia))

    def test_exemplo_11_5_Potter_SEM_BOMBA_FSOLVE(self):
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
            duto_AB = Duto(res_A, no_B, vazao_1, 0, 0, 50, 0.15, 0, 2, 0.26)
            duto_BC = Duto(no_B, res_C, vazao_2, 0, 0, 100, 0.10, 0, 1, 0.26)
            duto_BD = Duto(no_B, res_D, vazao_3, 0, 0, 300, 0.10, 0, 1, 0.26)

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
        self.assertTrue(numpy.allclose(solve(root), zeros, atol=self.tolerancia))


if __name__ == '__main__':
    unittest.main(verbosity=2)
