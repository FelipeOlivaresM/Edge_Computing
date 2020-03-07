#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import json

# This is the Subscriber

def on_connect(client, userdata, flags, rc):
  	print("Connected with result code "+str(rc))
  	client.subscribe("IA")

def on_message(client, userdata, msg):
	msg.payload = msg.payload.decode("utf-8")
	print("Sin decodificar")
	print(msg.payload)
	if msg.topic == "IA":
		print("Decodificado")
		payload = json.loads(msg.payload)
		print(payload)
		print("Despues")
		client.publish("AR", msg.payload)
		print("Publicado")

client = mqtt.Client()

client.connect("broker.mqttdashboard.com",1883)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()