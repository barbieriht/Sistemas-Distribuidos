import paho.mqtt.client as paho
from paho.mqtt import client as mqtt_client

import json

class CentroDeDistribuicao(object):
    def __init__(self):
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
                    return
                total = item['qtd']
                print(f'Não há unidades suficientes do produto {classe}. Total: {total} Pedido: {qtd}')
                return
        print(f'Produto {classe} não encontrado.')

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
        