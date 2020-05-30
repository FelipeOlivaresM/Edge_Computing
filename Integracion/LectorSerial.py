#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
import time
import serial
import re

def LecturaECG(N_datos):
    data = []
    # Iniciando conexión serial
    print("Inicia Lectura")
    arduinoPort = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    n=0
    # Retardo para establecer la conexión serial
    #time.sleep(1.8)

    while n < N_datos:
        getSerialValue = arduinoPort.readline()
        #getSerialValue = arduinoPort.read()
        #getSerialValue = arduinoPort.read(6)
        #print ('\nValor retornado de Arduino: %s' % (getSerialValue))
        x = re.findall("[0-9]{3}", str(getSerialValue))
        if len(x) > 0:
            data.append(x[0])
            n=n+1
    # Cerrando puerto serial
    arduinoPort.close()
    print(data)
    print(len(data))
    return data
