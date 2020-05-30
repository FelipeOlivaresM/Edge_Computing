import threading
import random
import paho.mqtt.client as paho
from LeerDataSet import leerDatos
from ejecucion import *
from LectorSerial import *
import simplejson as json
import time
from data_base import db as DB

broker = "broker.hivemq.com"
port = 1883
topicAI = "ECG"
topicAR = "testtopic/AR"
topicEot = "test/IA"
ia = False
info = '{"enfermedad":{"Nombre" : "", "Probablilidad" : 0}} '
datos = leerDatos()



ecg = ''
id_paciente= 1

client1 = paho.Client("DataParaIA")
client1.connect(broker, port , 3)
#t = threading.Thread(target=hola)
#t.start()

def on_message(client, userdata, msg):
    print("message")
    global info
    global ia
    data = msg.payload.decode("utf-8")
    info = json.loads(data)
    print(data)
    ia = True

def on_connect(client, userdata, flags, rc):
    client.subscribe(topicEot)
    

def Cinfig_mqtt():
    client1.on_message = on_message
    client1.on_connect = on_connect
    client1.connect(broker, port)
    client1.loop_forever()

def EnvioIA():
    global id_paciente
    while 1:
        time.sleep(3)
        ecg = LecturaECG(188)
        id_paciente=(id_paciente+1)%2
        #ecg = str(datos[random.randrange(0, len(datos))])
        #data_ia = "{'id':"+str(id_paciente)+", 'ecg':"+str(ecg)+"}"
        #data_ia = data_ia.replace("'", "\"")
        data_ia = {'id':str(id_paciente), 'ecg':ecg}
        print("Envio ini ia")
        
        client1.publish(topicAI , json.dumps(data_ia))#data_ia)
        print("Envio term ia")
        
        

def EnvioAR():
    global ia
    global info
    global broker
    db= DB()
    while True:
        if ia:
            
            bpm = random.randrange(45, 120)
            disease = info
            db.crear_registro(id_paciente, bpm, disease["name"], disease["probability"], ecg)
            data = db.historico(id_paciente)
            ar = json.dumps(data)#'{"enfermedad":"'+disease["name"]+'","probabilidad":'+str(disease["probability"]*100)+',"mensage":'+str(bpm)+'}'
            #ar = '{"enfermedad":"'+disease["name"]+'","probabilidad":'+str(disease["probability"]*100)+',"mensage":80}'
            print("Envio ini")
            client1.publish(topicAR+"/"+str(id_paciente), ar)
            ia = False
            print("Envio term")


h1 = threading.Thread(target=Cinfig_mqtt)
h2 = threading.Thread(target=EnvioAR)
h3 = threading.Thread(target=EnvioIA)
print("inicia Conexion")
h1.start()
print("inicia envio ia")
h3.start()
print("inicia envio AR")
h2.start()