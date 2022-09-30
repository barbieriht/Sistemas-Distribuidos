import random
import time
import json

import paho.mqtt.client as paho
from paho.mqtt import client as mqtt_client
from paho import mqtt

import sub
import pub

class Fabrica(object):
    #instancia fabrica com nome e lista de produtos
    def __init__(self, nome):
        self.id = random.randint(0, 1000)
        self.nome = nome
        self.produtos = []

    #insere produtos na fábrica (máximo de 3 classes de produto)
    def insereProduto(self, classe):
        if(len(self.produtos)<= 3):
            for item in self.produtos:
                if classe == item['classe']:
                    print(f'Produto {classe} já existe')
                    return
            self.produtos.append({'classe':classe})
            return
        print('Essa fábrica já tem o limite de produtos')

    def removeProduto(self, classe):
        if(len(self.produtos) > 0):
            for item in self.produtos:
                if classe == item['classe']:
                    self.produtos.remove(item)
                    print(f'Produto {classe} removido.')
                    with open('fabrica.json', 'w') as fp:
                        json.dump(self.produtos, fp)
                    return
            print(f'Produto {classe} não existe nessa fábrica.')
            return
        print('Não há produtos nessa fábrica.')

    #subtrai do estoque de produtos da fabrica
    def entregaProduto(self, classe, qtd):
        for item in self.produtos:
            if classe == item['classe']:
                print(f'{qtd} {classe}s entregues.')
                return True
        print(f'Produto {classe} não encontrado.')
        return False

if __name__ == "__main__":

    produtos = ['Pinga', 'Cerveja', 'Coxinha']

    loja1 = Fabrica('Fábrica da Esquina')
    i = 0
    while True:
        produto = produtos[random.randint(0,2)]
        if i == 0:
            for x in range(0,3):
                loja1.insereProduto(produtos[x])
        sub.run('fabrica')
        with open('fabrica.txt', 'r') as f:
            fabrica = f.read()
            fabrica = fabrica.split('$')
            f.close()
        for pedido in fabrica:
            this = pedido.split(';')
            pub.run('fabrica', str(this[0]) + ';' + this[1] + ';' + str(this[3] - this[2]) + '$' , f'Entregues {this[3] - this[2]} {this[0]}s para {this[0]}')
        i += 1
        time.sleep(3)