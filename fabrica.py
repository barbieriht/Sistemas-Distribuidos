import random
import time

import paho.mqtt.client as paho
from paho.mqtt import client as mqtt_client
from paho import mqtt

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

    #subtrai do estoque de produtos da fabrica
    def removeProduto(self, classe, qtd):
        for item in self.produtos:
            if classe == item['classe']:
                print(f'{qtd} {classe}s entregues para...')
                return True
        print(f'Produto {classe} não encontrado.')
        return False
    
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

    loja1 = Fabrica('Fábrica da Esquina')
    i = 0
    while True:
        produto = produtos[random.randint(0,2)]
        if i == 0:
            for x in range(0,3):
                loja1.insereProduto(produtos[x])
        loja1.removeProduto(produto, random.randint(0, 20))
        i += 1
        time.sleep(3)