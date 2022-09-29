from produto import Produto

class Loja(object):
    def __init__(self, nome):
        self.nome = nome
        self.produtos = []

    def insereProduto(self, classe, qtd, estoque):
        for item in self.produtos:
            if classe == item.classe:
                item.addQtd(qtd)
        else:
            self.produtos.append(Produto(classe, qtd, estoque))

    def removeProduto(self, classe, qtd):
        for item in self.produtos:
            if classe == item.classe:
                item.subQtd(qtd)
                return True
        else:
            return False

    def checaEstoque(self):
        for produto in self.produtos:
            if produto.getPct() >= 0.5:
                return 'verde'
            elif produto.getPct() >= 0.25:
                return 'amarelo'
            else:
                return 'vermelho'