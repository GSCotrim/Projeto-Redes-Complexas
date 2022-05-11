from DefinindoCoisas import *
from scipy.optimize import fsolve
import numpy as np

sistema = definindo_sistema()
eq = sistema.sistema_de_equacoes()

batata = 'lambda x : [' + ','.join(eq) + ']'

solve = eval(batata)
chute_inicial = np.array([0.5, 0.5, 0.5, 0.5])
root = fsolve(solve, chute_inicial)

print(np.isclose(solve(root), [0.0, 0.0, 0.0, 0.0]))

print(root)

