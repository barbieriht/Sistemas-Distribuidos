import paho.mqtt.client as paho
from paho.mqtt import client as mqtt_client

from loja import Loja
from fabrica import Fabrica

import json

import sub
import pub

sub.run('orders')