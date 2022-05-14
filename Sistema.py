from Nos import *
from Duto import *
from Reservatorio import *
import numpy as np


class Sistema(object):

    def __init__(self, dutos, nos):
        self.dutos = dutos
        self.nos = nos
        self.eq_energia = len(dutos)

    def give_nos_please(self):
        batata = list(filter(lambda xxx: type(xxx) is Nos, self.nos))
        return batata

    def give_reservatorios_please(self):
        batata = list(filter(lambda xxx: type(xxx) is Reservatorio, self.nos))
        return batata

    def give_nos_e_reservatorios_please(self):
        batata = list(filter(lambda xxx: type(xxx) is Nos or Reservatorio, self.nos))
        return batata

    def give_dutos_do_no_please(self, no):
        batata = list(filter(lambda xxx: xxx.no_inicial == no or xxx.no_final == no, self.dutos))
        return batata

    def give_dutos_do_no_por_nome_please(self, nome):
        batata = list(filter(lambda yyy: yyy.no_inicial.nome == nome or yyy.no_final.nome == nome, self.dutos))
        return batata

    def give_dutos_please(self):
        batata = list(filter(lambda xxx: type(xxx) is Duto, self.dutos))
        return batata

    # TODO: Limpar código. Tirar contador e ".append(0)"
    # Será que não vale a pena definir "duto_vazao_substituto" antes de entrar no for e só usar um "if", sem necessidade
    # de um "else"
    def equacoes_massa(self):
        funcoes_massa = []
        str_funcoes_massa = []  ##
        nos = self.give_nos_please()
        contador = -1
        for no in nos:
            contador += 1
            funcoes_massa.append(0)
            str_funcoes_massa.append('')  ##
            dutos = self.give_dutos_do_no_please(no)
            for duto in dutos:
                if duto.no_inicial == no:
                    duto_vazao_substituto = duto.vazao * -1

                else:
                    duto_vazao_substituto = duto.vazao

                funcoes_massa[contador] += duto_vazao_substituto

            funcoes_massa[contador] -= no.vazao_pontual

        return funcoes_massa

    def equacoes_energia(self):
        funcoes_energia = []
        dutos = self.give_dutos_please()
        for duto in dutos:
            funcoes_energia.append(
                duto.no_inicial.altura - duto.no_final.altura - duto.resistencia_hidraulica * duto.vazao * np.abs(
                    duto.vazao) + duto.valor_bomba)

        return funcoes_energia

    def sistema_de_equacoes(self):
        funcoes_massa = self.equacoes_massa()
        funcoes_energia = self.equacoes_energia()
        sistema_equacoes = []
        str_sistema_equacoes = []  ##
        for func in funcoes_massa:
            sistema_equacoes.append(func)
            str_sistema_equacoes.append(str(func))  ##

        for func in funcoes_energia:
            sistema_equacoes.append(func)
            str_eq = str(func)  ##
            str_sistema_equacoes.append(str_eq.replace('Abs', 'np.abs'))  ##

        return str_sistema_equacoes
