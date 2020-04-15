import threading #Hilos de ejecucion
import random # random para sacar un dato aleatorio del dataset
import paho.mqtt.client as paho #libreia de mqtt
from LeerDataSet import leerDatos # carha el archivo del dataset
from LectorSerial import * #Lector serial
import simplejson as json # tratamiento de las tramas
import time # Detener hilos

broker = "broker.mqttdashboard.com"
port = 1883
topicAI = "ECG"
topicAR = "testtopic/AR"
topicEot = "test/IA"
ia = False
info = '{"enfermedad":{"Nombre" : "", "Probablilidad" : 0}} '
datos = leerDatos()


def on_message(client, userdata, msg):
    print("message")
    global info
    global ia
    data = msg.payload.decode("utf-8")
    info = json.loads(data)
    print(data)
    ia = True #Cuando recibe un dato de IA cambia para poder enviar a AR

def on_connect(client, userdata, flags, rc):
    client.subscribe(topicEot)
    

def Cinfig_mqtt(): #Hilo espera lo que publica IA
    client1 = paho.Client("DataFromIA")
    client1.on_message = on_message
    client1.on_connect = on_connect
    client1.connect(broker, port)
    client1.loop_forever()

def EnvioIA(): #Hilo Publica datos a IA
    while 1:
        time.sleep(8) #Espera para no enviar siempre a IA
        ecg = LecturaECG(188) #Recoje 188 datos del sensor (Se puede comentar para pruevas)
        ecg = str(datos[random.randrange(0, len(datos))])  #Extae un registro aleatorio del dataset
        data_ia = "{'ecg':"+ecg+"}" #tama para IA
        data_ia = data_ia.replace("'", "\"") # Formato para enviar
        print("Envio ini ia")
        client1 = paho.Client("DataToIA")
        client1.connect(broker, port , 3)
        client1.publish(topicAI ,data_ia)
        print("Envio term ia")
        
        

def EnvioAR(): #Hilo para envial datos a AR
    global ia
    global info
    global broker
    while True:
        if ia:
            bpm = random.randrange(45, 120) #random de bpm
            disease = info #Informacion capturada de IA
            ar = '{"enfermedad":"'+disease["name"]+'","probabilidad":'+str(disease["probability"]*100)+',"mensage":'+str(bpm)+'}' #Crea la trama para publica a AR
            #ar = '{"enfermedad":"'+disease["name"]+'","probabilidad":'+str(disease["probability"]*100)+',"mensage":80}'
            #print("Envio ini")
            client1 = paho.Client("DataParaAR")
            client1.connect(broker, port , 3)
            client1.publish(topicAR,ar)
            ia = False #Cambia para que no siga enviando 
            print("Envio term")
            
"""Cracion de los Hilos"""

h1 = threading.Thread(target=Cinfig_mqtt) # Recive de IA
h2 = threading.Thread(target=EnvioAR) # Publica a IA
h3 = threading.Thread(target=EnvioIA) # Puplica a AP

"""Inicio de los Hilos"""

print("inicia Conexion")
h1.start()
print("inicia envio ia")
h3.start()
print("inicia envio AR")
h2.start()
