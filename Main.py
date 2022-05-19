from Solver import *
from DefinindoCoisas import *


# Hipoteses:
#  - Regime Permanente
#  - Incompressivel
#  - Newtoniano
#  - Modelo Darcy
#  - Delta Energia Cinetica = 0
#  - Reservatorios grandes
#  - Pressurizada

# UNIDADES: SI


def main():
    sistema = definindo_sistema()
    eq = sistema.sistema_de_equacoes()
    solver = Solver(eq)
    func = solver.func()
    solver.solve_system(func)


main()

