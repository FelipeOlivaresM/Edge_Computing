#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
import time
import serial

# Iniciando conexión serial
arduinoPort = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
flagCharacter ='k'

# Retardo para establecer la conexión serial
time.sleep(1.8) 
while True:
	getSerialValue = arduinoPort.readline()
	#getSerialValue = arduinoPort.read()
	#getSerialValue = arduinoPort.read(6)
	print ('\nValor retornado de Arduino: %s' % (getSerialValue))

# Cerrando puerto serial
arduinoPort.close()
