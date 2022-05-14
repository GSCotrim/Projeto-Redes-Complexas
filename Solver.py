from DefinindoCoisas import *
from scipy.optimize import fsolve
import numpy as np


class Solver(object):

    def __init__(self, eq):
        self.eq = eq

    def func(self):
        return 'lambda x : [' + ','.join(self.eq) + ']'

    # func = 'lambda x : [' + ','.join(self.eq) + ']'

    def solve_system(self, func):
        size = len(self.eq)
        chute_inicial = np.ones(size)

        for i in range(size):
            chute_inicial[i] = 0.5 * chute_inicial[i]

        solve = eval(func)
        root = fsolve(solve, chute_inicial)

        print(np.isclose(solve(root), [0.0, 0.0, 0.0, 0.0]))
        print(root)

        return root
