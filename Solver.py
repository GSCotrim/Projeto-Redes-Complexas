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
            chute_inicial[i] = 10 * chute_inicial[i]

        func = func.replace('log', 'np.log10') ##
        solve = eval(func)
        root = fsolve(solve, chute_inicial)
        x, infodict, ier, mesg = fsolve(solve, chute_inicial, full_output=True) ##

        return root, solve
