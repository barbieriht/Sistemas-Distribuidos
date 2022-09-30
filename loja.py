import time
import random

import paho.mqtt.client as paho
from paho import mqtt
from paho.mqtt import client as mqtt_client

import json

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
                total = item['qtd'] + qtd
                item['qtd'] = total
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
                    #print(f'Produto {classe} em estado verde')
                    return 'verde'
                elif pct >= 0.25:
                    #print(f'Produto {classe} em estado amarelo')
                    return 'amarelo'
                else:
                    #print(f'Produto {classe} em estado vermelho')
                    return 'vermelho'

    def connect_mqtt(self):
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                print("Connected to MQTT Broker!")
            else:
                print("Failed to connect, return code %d\n", rc)

        self.client = mqtt_client.Client(self.id)
        self.client.username_pw_set('admin', 'hivemq')
        self.client.on_connect = on_connect
        self.client.connect(self.broker, self.port)
        return self.client


    def publish(self, topic, msg):
        result = self.client.publish(topic, msg)
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")

    def subscribe(self, client: mqtt_client, topic):
        def on_message(client, userdata, msg):
            print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

        self.client.subscribe(topic)
        self.client.on_message = on_message

if __name__ == "__main__":

    produtos = ['Pinga', 'Cerveja', 'Coxinha']

    loja1 = Loja('Bar do Zé')
    i = 0
    while True:
        produto = produtos[random.randint(0,2)]
        if i == 0:
            for x in range(0,3):
                loja1.insereProduto(produtos[x], 50, 50)
        loja1.removeProduto(produto, random.randint(0, 20))
        estado = loja1.checaEstoque(produto)
        if(estado == 'vermelho' or i == 0):
            loja1.insereProduto(produtos[random.randint(0,2)], random.randint(20, 50), 50)
        i += 1
        time.sleep(3)
    