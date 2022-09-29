from loja import Loja

class Consumidor(object):
    #instancia consumidor pelo nome
    def __init__(self, nome):
        self.nome = nome
        self.lojas = []

    #compra determinada quantidade de determinada classe de produtos de determinada loja
    def compraProduto(self, nome_loja, classe_produto, qtd):
        for loja in self.lojas:
            if loja.nome == nome_loja:
                loja.removeProduto(classe_produto, qtd)
                return True
        else:
            print('Couldn\'t find this store')
            return False


