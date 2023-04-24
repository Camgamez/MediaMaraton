import sqlite3
from sqlite3 import Error
from datetime import datetime
import re
def conexion_sql():
    try:
        con = sqlite3.connect('BDSQlLiteEjercicioClase.db')
        return con
    except Error:
        print(Error)

def tabla_atleta(con):
        cursorObj = con.cursor()
        cursorObj.execute('''CREATE TABLE IF NOT EXISTS atleta(
                          no_id_atleta INTEGER,
                          no_inscripcion text,
                          nombre text, 
                          apellido text, 
                          correo text, 
                          fecha_de_nacimiento date,
                          pais_origen, 
                          ciudad_origen, 
                          PRIMARY KEY(no_id_atleta,no_inscripcion))
                          ''')#Tabla falta foto
        con.commit()

def tabla_carrera(con):
        cursorObj = con.cursor()
        cursorObj.execute('''CREATE TABLE IF NOT EXISTS carrera(
                          no_evento INTEGER PRIMARY KEY,
                          ano INTEGER,
                          premio_primer_puesto text, 
                          premio_segundo_puesto text, 
                          premio_tercer_puesto text) 
                          ''')#reproduce canción
        con.commit()

def tabla_resultado_carrera(con):
    if con is not None:
      cursorObj = con.cursor()
      cursorObj.execute('''CREATE TABLE IF NOT EXISTS resultado_carrera(
                        no_evento integer,
                        no_inscripcion integer, 
                        posicion integer,
                        tiempo_empleado TIME CHECK(tiempo_empleado LIKE '__:__'),
                        indicador_resultado char(1),
                        PRIMARY KEY(no_evento,no_inscripcion))''')
      con.commit()

def tabla_clasificacion_final(con):
        cursorObj = con.cursor()
        cursorObj.execute('''CREATE TABLE IF NOT EXISTS clasificacion_final(
                          no_inscripcion INTEGER PRIMARY KEY,
                          no_evento INTEGER,
                          nombre text, 
                          apellido text, 
                          fecha_de_nacimiento date,
                          pais_origen text, 
                          ciudad_origen text, 
                          tiempo_empleado TIME 
                          )''')#Tabla falta foto
        con.commit()

def insertar_tabla_atleta(con):
    cursorObj = con.cursor()
    no_id_atleta = input("Numero identificacion del atleta: ")
    no_id_atleta = no_id_atleta.ljust(12)
    if in_db(con,"no_id_atleta",no_id_atleta,"atleta") is None:
      while True:
        try:
          no_inscripcion = int(input("Numero inscripcion atleta: "))
          break
        except ValueError:
           print("Numero inscripcion invalido")

      if in_db(con,"no_inscripcion",no_inscripcion,"atleta") is None:
        while True:
          nombre = input("Nombre atleta: ").upper()
          nombre = nombre.ljust(12)
          if re.findall("[`!@#$%^&*()_+\-=\[\]{};':\\|,.<>\/?~\d]", nombre) != []:
              print("Nombre invalido.")
          else:
              break

        while True:
          apellido = input("Apellido atleta: ").upper()
          apellido = apellido.ljust(12)
          if re.findall("[`!@#$%^&*()_+\-=\[\]{};':\\|,.<>\/?~\d]", apellido) != []:
              print("Apellido invalido.")
          else:
              break

        while True:
          correo = input("Correo atleta: ").upper()
          if re.findall(".{1}@", correo) != []:
            break
          else:
              print("Correo invalido.")

        while True:
          try:
            fecha_de_nacimiento = input("Fecha de Nacimiento AAAA-MM-DD  ")
            fecha_de_nacimiento = datetime.strptime(fecha_de_nacimiento,"%Y-%m-%d").date()
            break
          except ValueError:
            print("Fecha invalida.")
        
        while True:
          pais_origen = input("País origen: ").upper()
          pais_origen = pais_origen.ljust(12)
          if re.findall("[`!@#$%^&*()_+\-=\[\]{};':\\|,.<>\/?~\d]", pais_origen) != []:
              print("Pais invalido.")
          else:
              break
          
        while True:
          ciudad_origen = input("Ciudad origen: ").upper()
          ciudad_origen = ciudad_origen.ljust(12)
          if re.findall("[`!@#$%^&*()_+\-=\[\]{};':\\|,.<>\/?~\d]", ciudad_origen) != []:
              print("Ciudad invalida.")
          else:
              break
        
        cad = f'''INSERT INTO atleta VALUES(
              '{no_id_atleta}',
              '{no_inscripcion}',
              '{nombre}',
              '{apellido}',
              '{correo}',
              '{fecha_de_nacimiento}',
              '{pais_origen}',
              '{ciudad_origen}'
              )'''
        cursorObj.execute(cad)
        con.commit()
      else:
          print(f"Atleta con No Inscripcion {no_inscripcion} ya existe.")
    else:
      print(f"Atleta identificado con {no_id_atleta} ya existe.")
      #Devolver al menú

def in_db(con_sql,column,attribute,table):
    cursor = con_sql.cursor()
    check=f"SELECT {column} FROM {table} where {column} = '{attribute}'"
    cursor.execute(check)
    return cursor.fetchone()

def consultar_tabla_atletas(con):
    cursorObj = con.cursor()
    id_consultada = input("Ingrese su documento de identificacion: ")
    cad = f'''SELECT * FROM atleta where no_id_atleta like "%{id_consultada}%" '''
    cursorObj.execute(cad)
    lista = cursorObj.fetchall()
    for row in lista:
        no_id_atleta = row[0]
        no_inscripcion = row[1]
        nombre = row[2]
        apellido = row[3]  
        correo = row[4]
        fecha_de_nacimiento = row[5]
        pais_origen = row[6]
        ciudad_origen = row[7]
        print(f'''Numero de identificacion del atleta: {no_id_atleta}
                Numero de inscripcion del atleta: {no_inscripcion}
                Nomble del atleta: {nombre}
                Apellido del atleta: {apellido}
                Correo del atleta: {correo}
                Fecha de nacimiento del atleta: {fecha_de_nacimiento}
                Pais de origen del atleta: {pais_origen}
                Ciudad de origen del atleta: {ciudad_origen}
              ''')
    if not lista:
        print("No se encontraron resultados.")


def actualizar_tabla_atleta(con):
  cursorObj = con.cursor()
  no_id_atleta=input("Ingrese identificacion de atleta  a consultar: ")
  while True:
    nombre = input("Nuevo nombre atleta: ").upper()
    nombre = nombre.ljust(12)
    if re.findall("[`!@#$%^&*()_+\-=\[\]{};':\\|,.<>\/?~\d]", nombre) != []:
      print("Nombre invalido.")
    else:
      break

  while True:
    apellido = input("Nuevo apellido atleta: ").upper()
    apellido = apellido.ljust(12)
    if re.findall("[`!@#$%^&*()_+\-=\[\]{};':\\|,.<>\/?~\d]", apellido) != []:
      print("Apellido invalido.")
    else:
      break

  cad=f'''UPDATE atleta set nombre = "{nombre}", apellido = "{apellido}"
          where no_id_atleta like "%{no_id_atleta}%" '''
  cursorObj.execute(cad)
  con.commit()
  
def crear_carrera(con):
    cursorObj = con.cursor()
    while True:
        try:
          no_evento = int(input("Numero de evento: "))
          break
        except ValueError:
           print("Numero de evento invalido")
    
    if in_db(con,"no_evento",no_evento,"carrera") is None:
      while True:
        ano = input("Año evento: ").upper()
        ano = ano.ljust(4)
        try:
           ano = int(ano)
           break
        except ValueError:
           print("Ano invalido")

      premio_primer_puesto = input("Premio primer puesto: ").upper()
      premio_primer_puesto = premio_primer_puesto.ljust(12)
      premio_segundo_puesto = input("Premio segundo puesto: ").upper()
      premio_segundo_puesto = premio_segundo_puesto.ljust(12)
      premio_tercer_puesto = input("Premio tercer puesto: ").upper()
      premio_tercer_puesto = premio_tercer_puesto.ljust(12)
      cad = f'''INSERT INTO carrera VALUES(
                '{no_evento}',
                '{ano}',
                '{premio_primer_puesto}',
                '{premio_segundo_puesto}',
                '{premio_tercer_puesto}'
            )''' 
      cursorObj.execute(cad)
      con.commit()
    else:
      print(f"El número evento ya existe {no_evento}.")

def crear_resultado(con):
    cursorObj = con.cursor()
    while True:
        try:
          no_inscripcion = int(input("Numero inscripcion atleta: "))
          break
        except ValueError:
           print("Numero inscripcion invalido")

    while True:
        try:
          no_evento = int(input("Numero de evento: "))
          break
        except ValueError:
           print("Numero de evento invalido")
    
    if in_db(con,"no_inscripcion",no_inscripcion,"atleta") and in_db(con,"no_evento",no_evento,"carrera") is not None:
      while True:
        try:
          posicion = int(input("Numero posicion: "))
          break
        except ValueError:
           print("Numero de posición invalido")
      
      tiempo_empleado = input("Tiempo empleado HH:MM : ")
      while True:
        indicador_resultado = input(" Retirado'R', Descalificado'D', Finalizado'F': ").upper()
        if indicador_resultado == "R" or indicador_resultado == "D" or indicador_resultado == "F":
           break
        else:
           print("Indicador del resultado invalido")

      cad = f'''INSERT INTO resultado_carrera VALUES(
                '{no_inscripcion}',
                '{no_evento}',
                '{posicion}',
                '{tiempo_empleado}',
                '{indicador_resultado}'
            )''' 
      id_consultada = input("Ingrese su documento de identificacion: ")
      cad2 = f'''SELECT * FROM atleta where no_id_atleta like "%{id_consultada}%" '''
      cursorObj.execute(cad2)
      lista = cursorObj.fetchall()
      for row in lista:
          nombre = row[2]
          apellido = row[3]  
          fecha_de_nacimiento = row[5]
          pais_origen = row[6]
          ciudad_origen = row[7]
      cad3 = f'''INSERT INTO clasificacion_final VALUES(
                '{no_inscripcion}',
                '{no_evento}',
                '{nombre}',
                '{apellido}',
                '{fecha_de_nacimiento}',
                '{pais_origen}',
                '{ciudad_origen}',
                '{tiempo_empleado}'
              )'''
      cursorObj.execute(cad)
      cursorObj.execute(cad3)
      con.commit()
    else:
      print(f"El número evento ya existe {no_evento} y/o el número participante ya existe {no_inscripcion}.") 

def actualizar_resultado(con):
  cursorObj = con.cursor()
  while True:
        try:
          no_inscripcion = int(input("Numero inscripcion atleta a actualizar resultado: "))
          break
        except ValueError:
           print("Numero inscripcion invalido")

  while True:
        try:
          posicion = int(input("Numero posicion: "))
          break
        except ValueError:
           print("Numero de posición invalido")

  tiempo_empleado = input("Tiempo empleado HH:MM : ")
  while True:
        indicador_resultado = input(" Retirado'R', Descalificado'D', Finalizado'F': ").upper()
        if indicador_resultado == "R" or indicador_resultado == "D" or indicador_resultado == "F":
           break
        else:
           print("Indicador del resultado invalido")
  
  cad=f'''UPDATE resultado_carrera set posicion = "{posicion}",
           tiempo_empleado = "{tiempo_empleado}",
           indicador_resultado ="{indicador_resultado}"
          where no_inscripcion like "%{no_inscripcion}%" '''
  cursorObj.execute(cad)
  con.commit()


def registrar_atletas_descalificados(con):
  cursorObj = con.cursor()
  while True:
    try:
      no_inscripcion = int(input("Numero inscripcion atleta a consultar: "))
      break
    except ValueError:
       print("Numero inscripcion invalido")

  while True:
    indicador_resultado = input(" Retirado'R', Descalificado'D', Finalizado'F': ").upper()
    if indicador_resultado == "R" or indicador_resultado == "D" or indicador_resultado == "F":
      break
    else:
       print("Indicador del resultado invalido")
  cad=f'''UPDATE resultado_carrera set indicador_resultado = "{indicador_resultado}"
          where no_inscripcion like "%{no_inscripcion}%" '''
  cursorObj.execute(cad)
  con.commit()

def consultarClasificacion(con):
    cursorObj = con.cursor()
    while True:
        try:
          no_evento = int(input("Numero de evento: "))
          break
        except ValueError:
           print("Numero de evento invalido")
    
    cursorObj.execute(f"SELECT * FROM clasificacion_final WHERE no_evento = {no_evento} ORDER BY tiempo_empleado ASC")
    lista = cursorObj.fetchall()
    print(lista)

def main():
    con=conexion_sql()
    tabla_atleta(con)
    tabla_carrera(con)
    tabla_resultado_carrera(con)
    tabla_clasificacion_final(con)
    insertar_tabla_atleta(con)
    consultar_tabla_atletas(con)
    actualizar_tabla_atleta(con)
    crear_carrera(con)
    crear_resultado(con)
    actualizar_resultado(con)
    registrar_atletas_descalificados(con)
    consultarClasificacion(con)
    con.close()
main()