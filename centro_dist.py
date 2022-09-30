import paho.mqtt.client as paho
from paho.mqtt import client as mqtt_client

from loja import Loja
from fabrica import Fabrica

import json

import sub
import pub

loja = []
fabrica = []

while True:
    sub.run('loja')
    sub.run('fabrica')

    with open('loja.txt', 'r') as f:
        loja = f.read()
        loja = loja.split('$')
        f.close()
    for pedido in loja:
        pub.run('fabrica', pedido, 'Pedido!')
        loja.remove(pedido)
    
    with open('fabrica.txt', 'r') as f:
        fabrica = f.read()
        fabrica = fabrica.split('$')
        f.close()
    for entrega in fabrica:
        pub.run('loja', entrega, 'Pedido!')
        fabrica.remove(entrega)