from loja import Loja

class Consumidor(object):
    def __init__(self, nome):
        self.nome = nome
        self.lojas = []

    def compraProduto(self, nome_loja, classe_produto, qtd):
        for loja in self.lojas:
            if loja.nome == nome_loja:
                loja.removeProduto(classe_produto, qtd)
                return True
        else:
            print('Couldn\'t find this store')
            return False


