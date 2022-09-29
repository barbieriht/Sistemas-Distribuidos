from produto import Produto

class Loja(object):
    #instancia loja com nome
    def __init__(self, nome):
        self.nome = nome
        self.produtos = []

    #insere produto na loja de acordo com a classe desejada (compra)
    def insereProduto(self, classe, qtd, estoque):
        for item in self.produtos:
            if classe == item.classe:
                item.addQtd(qtd)
        else:
            self.produtos.append(Produto(classe, qtd, estoque))

    #remove produto de acordo com a classe desejada (venda)
    def removeProduto(self, classe, qtd):
        for item in self.produtos:
            if classe == item.classe:
                item.subQtd(qtd)
                return True
        else:
            return False

    #checa se o estoque precisa de reposição
    def checaEstoque(self):
        for produto in self.produtos:
            if produto.getPct() >= 0.5:
                return 'verde'
            elif produto.getPct() >= 0.25:
                return 'amarelo'
            else:
                return 'vermelho'