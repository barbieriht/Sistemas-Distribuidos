from produto import Produto

class Fabrica(object):
    #instancia fabrica com nome e lista de produtos
    def __init__(self, nome):
        self.nome = nome
        self.produtos = []

    #insere produtos na fábrica (máximo de 3 classes de produto)
    def insereProduto(self, classe, qtd, estoque):
        if(len(self.produtos <= 3)):
            for item in self.produtos:
                if classe == item.classe:
                    item.addQtd(qtd)
            else:
                self.produtos.append(Produto(classe, qtd, estoque))
            return True
        print('You can\'t add more products in this factory')
        return False

    #subtrai do estoque de produtos da fabrica
    def removeProduto(self, classe, qtd):
        for item in self.produtos:
            if classe == item.classe:
                if(item.qtd < qtd):
                    print('There\'s not enough stock of this product')
                    return False
                item.subQtd(qtd)
                return True
        else:
            print('Couldn\'t find this product')
            return False