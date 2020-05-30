#from EnvioDeDatos import *
import json
def hola():
    while True:
        global ia
        global info
        if ia:
            imprimir_enf(info)
            ia=False
 
def imprimir_enf(dato):
    parsed_json = json.loads(dato)
    print(parsed_json["enfermedad"])
    print("________")