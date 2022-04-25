from DefinindoCoisas import *
from Sistema import *
from scipy.optimize import fsolve
import numpy as np


# Hipoteses:
#  - Regime Permanente
#  - Incompressivel
#  - Newtoniano
#  - Modelo Darcy
#  - Delta Energia Cinetica = 0
#  - Reservatorios grandes
#  - Pressurizada

def main():
    definindo_sistema()


# def f(xyzw):
#     vazao_1 = xyzw[0]
#     vazao_2 = xyzw[1]
#     vazao_3 = xyzw[2]
#     altura_B = xyzw[3]
#
#     sistema_eq = np.array([vazao_1 - vazao_2 - vazao_3,
#                            -altura_B - 1420.0 * vazao_1 * abs(vazao_1) + 10,
#                            altura_B - 13200.0 * vazao_2 * abs(vazao_2) - 15,
#                            altura_B - 62800.0 * vazao_3 * abs(vazao_3) - 30])
#     return sistema_eq
#
#
# chute_inicial = np.array([0.5, 0.5, 0.5, 0.5])
# xyzw = fsolve(f, chute_inicial)
#
# vazao_1 = xyzw[0]
# vazao_2 = xyzw[1]
# vazao_3 = xyzw[2]
# altura_B = xyzw[3]
#
# print(vazao_1, vazao_2, vazao_3, altura_B, f(xyzw))

main()
