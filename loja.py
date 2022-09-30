import time
import random

import paho.mqtt.client as paho
from paho import mqtt
from paho.mqtt import client as mqtt_client

import json

import sub
import pub

class Loja(object):
    #instancia loja com nome
    def __init__(self, nome):
        self.id = random.randint(0, 1000)
        self.nome = nome
        self.broker = 'broker.emqx.io'
        self.port = 1883
        self.produtos = []
        
    #insere produto na loja de acordo com a classe desejada (compra)
    def insereProduto(self, classe, qtd, estoque=0):
        for item in self.produtos:
            if classe == item['classe']:
                pub.run('loja', str(self.id) + ';' + item['classe'] + ';' + str(item['qtd']) + ';' + str(item['estoque']) + '$', f'{qtd} {classe}s order')
                sub.run('loja')
                with open('loja.txt', 'r') as f:
                    loja = f.read()
                    loja = loja.split('$')
                
                with open('loja.txt', 'w') as f:
                    for pedido in loja:
                        if pedido[0] == self.id and pedido[1] == classe:
                            total = item['qtd'] + pedido[2]
                            item['qtd'] = total
                            loja.remove(pedido)
                        else:
                            f.write(pedido[0] + ';' + pedido[1] + ';' + pedido[2] + '$')
                print(f'Adicionadas {qtd} unidades ao produto {classe}. Total: {total}')
                return
        self.produtos.append({'classe':classe, 'qtd':qtd, 'estoque':estoque})

    #remove produto de acordo com a classe desejada (venda)
    def removeProduto(self, classe, qtd):
        for item in self.produtos:
            if classe == item['classe']:
                if(qtd <= item['qtd']):
                    total = item['qtd'] - qtd
                    item['qtd'] = total
                    print(f'Removidas {qtd} unidades do produto {classe}. Total: {total}')
                    self.checaEstoque(classe)
                    return True
                total = item['qtd']
                print(f'Não há unidades suficientes do produto {classe}. Total: {total} Pedido: {qtd}')
                return True
        print(f'Produto {classe} não encontrado.')
        return False

    #checa se o estoque precisa de reposição
    def checaEstoque(self, classe):
        for produto in self.produtos:
            if produto['classe'] == classe:
                pct = produto['qtd']/produto['estoque']
                if pct >= 0.5:
                    return 'verde'
                elif pct >= 0.25:
                    return 'amarelo'
                else:
                    self.insereProduto(classe, produto['estoque'] - produto['qtd'])
                    return 'vermelho'

if __name__ == "__main__":

    produtos1 = ['Pinga', 'Cerveja', 'Corote']
    produtos2 = ['Salsicha', 'Molho', 'Batata']

    loja1 = Loja('Bar do Zé')
    loja2 = Loja('Podrão da Praça')

    i = 0
    while True:
        if i == 0:
            for x in range(0,3):
                loja1.insereProduto(produtos1[x], 50, 50)
                loja2.insereProduto(produtos2[x], 50, 50)

        produto = produtos1[random.randint(0,2)]
        loja1.removeProduto(produto, random.randint(0, 20))
        estado = loja1.checaEstoque(produto)
        if(estado == 'vermelho' or i == 0):
            loja1.insereProduto(produtos1[random.randint(0,2)], random.randint(20, 50), 50)

        produto = produtos2[random.randint(0,2)]
        loja2.removeProduto(produto, random.randint(0, 20))
        estado = loja2.checaEstoque(produto)
        if(estado == 'vermelho' or i == 0):
            loja2.insereProduto(produtos2[random.randint(0,2)], random.randint(20, 50), 50)
        time.sleep(3)
        i += 1

