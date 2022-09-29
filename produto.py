class Produto(object):
    def __init__(self, classe, qtd, estoque):
        self.classe = classe
        self.qtd = qtd
        self.estoque = estoque

    def getClasse(self):
        return self.classe

    def getEstoque(self):
        return self.estoque

    def getPct(self):
        return self.qtd/self.estoque

    def getQtd(self):
        return self.qtd

    def addQtd(self, qtd):
        self.qtd += qtd

    def subQtd(self, qtd):
        self.qtd -= qtd

    def setEstoque(self, estoque):
        self.estoque = estoque