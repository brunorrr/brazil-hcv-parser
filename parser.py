import numpy as np
import pandas as pd

class Cidade:
    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome
    def __repr__(self):
        return "Cidade(%s, %s)" % (self.codigo, self.nome)
    def __eq__(self, other):
        if isinstance(other, Cidade):
            return (other.codigo == self.codigo)
        else:
            return False
    def __ne__(self, other):
        return (not self.__eq__(other))
    def __hash__(self):
        return hash(self.__repr__())

file = open('temp/csv/opera_presta_nao_hospitalares_202201_MA.csv',encoding='latin-1')
separator = file.read(14)[13]
file.close()

data = pd.read_csv('temp/csv/opera_presta_nao_hospitalares_202201_MA.csv',encoding='latin-1',sep=separator)


