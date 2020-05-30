import sqlite3

class db:
    def __init__(self):
        self.con = sqlite3.connect('mydatabase.db')
        self.cursorObj = self.con.cursor()
        self.crear_tabla()
    
    def crear_tabla(self):
        atributos = "id integer, registro integer, bpm integer, enfermedad text, probabilida doble, ecg text"
        sql = 'create table if not exists paciente({})'.format(atributos)
        self.cursorObj.execute(sql)
        self.con.commit()
        
    def insertar(self, id, registro, bpm, enfermedad, probabilida, ecg):
        values = "{}, {}, {}, '{}', {}, '{}'".format(id, registro, bpm, enfermedad, probabilida, str(ecg))
        sql="INSERT INTO paciente VALUES({})".format(values)
        self.cursorObj.execute(sql)
        self.con.commit()
    
    def crear_registro(self, id, bpm, enfermedad, probabilida, ecg):
        registro = 2
        
        
        sql = 'DELETE FROM paciente WHERE id={} and registro={}'.format(id, 0)
        print(sql)
        self.cursorObj.execute(sql)
        
        sql="UPDATE paciente SET registro={} WHERE id={} and registro={}".format(0,id,1)
        self.cursorObj.execute(sql)
        
        sql="UPDATE paciente SET registro={} WHERE id={} and registro={}".format(1,id,2)
        self.cursorObj.execute(sql)
        
        self.insertar(id, registro, bpm, enfermedad, probabilida, ecg)
        
    def historico(self, id):
        sql="SELECT * FROM paciente WHERE id={}".format(id)
        self.cursorObj.execute(sql)
        
        datos=[]
        
        rows = self.cursorObj.fetchall()
        for row in rows:
            registro = {#'id': row[0],
                        #'bpm': str(row[2]),
                        'enfermedad':row[3],
                        'probabilidad': str(format(row[4]*100, '0.2f')),
                        'mensage': str(row[2]) }
            datos.append(registro)
        return datos
            

#db= db()

#db.crear_registro(1, 210, 'Frio', 0.50, 'hola!! 2')

#print(db.historico(1))



    
    