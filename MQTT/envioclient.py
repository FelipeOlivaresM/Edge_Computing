#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import json

# This is the Subscriber

def on_connect(client, userdata, flags, rc):
	print("Connected with result code "+str(rc))
	client.subscribe("IA")
	client.publish("IA", json.dumps({'genre': ['Action', 'Comedy']}))


client = mqtt.Client()
client.connect("broker.mqttdashboard.com",1883)


client.on_connect = on_connect

client.loop_forever()