class Nos(object):

    def __init__(self, nome, altura, vazao_pontual):
        self.altura = altura
        self.vazao_pontual = vazao_pontual
        self.nome = nome

    def __str__(self):
        return f'\033[91m{self.nome}\033[0m'

    def __repr__(self):
        return self.__str__()


