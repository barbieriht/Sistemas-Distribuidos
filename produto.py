class Produto(object):
    #ao instanciar o produto já setamos sua classe, quantidade e padrão de estoque
    def __init__(self, classe, qtd, estoque):
        self.classe = classe
        self.qtd = qtd
        self.estoque = estoque

    #recebe classe
    def getClasse(self):
        return self.classe

    #recebe estoque
    def getEstoque(self):
        return self.estoque

    #recebe quantidade de itens disponíveis
    def getQtd(self):
        return self.qtd

    #recebe porcentagem do estoque disponível
    def getPct(self):
        return self.qtd/self.estoque

    #adiciona quantidade (compra)
    def addQtd(self, qtd):
        self.qtd += qtd

    #subtrai quantidade (venda)
    def subQtd(self, qtd):
        self.qtd -= qtd

    #modifica o padrão de estoque
    def setEstoque(self, estoque):
        self.estoque = estoque