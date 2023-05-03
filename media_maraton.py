'''Las siguientes siguientes librerias son las usadas en el programa:
  -sqlite 3 para el manejo de la base de datos.
  -datetime para el manejo del formato de la fecha ingresada por el usuario y 
    almacenamiento en la base de datos.
  -re para la iteración de una cadena de texto para buscar coincidencias. ''' 

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

'''La anterior función se encarga de la creación del cursor encargado de recorrer
    la tabla, además archivo de la base de datos si este no existe, sí ya existe
    se conecta a dicho archivo. Dado el caso que no se de ninguno 
    de los casos presentados imprime en pantalla el error. ''' 

def tabla_atleta(con): #Creación de la tabla atleta sí no existe, sino sigue. 
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
                          ''')  # Tabla falta foto
    con.commit()

'''La anterior función crea la tabla atleta en el archivo BDSQlLiteEjercicioClase.db
    por medio del cursorObj el cual ejecuta el comando SQL y posterior a ello hace
    commit para salvaguardar dicha creación, dado el caso que exista la tabla, la
    función no realiza nada. ''' 

def tabla_carrera(con): #Creación de la tabla carrera si no existe, sino sigue. 
    cursorObj = con.cursor()
    cursorObj.execute('''CREATE TABLE IF NOT EXISTS carrera(
                          no_evento INTEGER PRIMARY KEY,
                          ano INTEGER,
                          premio_primer_puesto text, 
                          premio_segundo_puesto text, 
                          premio_tercer_puesto text) 
                          ''')  # reproduce canción
    con.commit()

'''La anterior función crea la tabla carrera en el archivo BDSQlLiteEjercicioClase.db
    por medio del cursorObj el cual ejecuta el comando SQL y posterior a ello hace
    commit para salvaguardar dicha creación, dado el caso que exista la tabla, la
    función no realiza nada. ''' 

def tabla_resultado_carrera(con): #Creación de la tabla resultado carrera si no existe, sino sigue.
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

'''La anterior función crea la tabla resultado carrera en el archivo 
    BDSQlLiteEjercicioClase.db por medio del cursorObj el cual ejecuta el comando 
    SQL y posterior a ello hace commit para salvaguardar dicha creación, dado el 
    caso que exista la tabla, la función no realiza nada. ''' 

def tabla_clasificacion_final(con): #Creación de la tabla clasificación final si no existe, sino sigue.
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
                          )''')  # Tabla falta foto
    con.commit()

'''La anterior función crea la tabla clasificación final en el archivo 
    BDSQlLiteEjercicioClase.db por medio del cursorObj el cual ejecuta el comando 
    SQL y posterior a ello hace commit para salvaguardar dicha creación, dado el 
    caso que exista la tabla, la función no realiza nada. '''

def insertar_tabla_atleta(con):
    cursorObj = con.cursor()
    no_id_atleta = input("Numero identificacion del atleta: ")
    no_id_atleta = no_id_atleta.ljust(12)
    if in_db(con, "no_id_atleta", no_id_atleta, "atleta") is None:

        while True:
            try:
                no_inscripcion = int(input("Numero inscripcion atleta: "))
                break
            except ValueError:
                print("Numero inscripcion invalido")

        if in_db(con, "no_inscripcion", no_inscripcion, "atleta") is None:
            nombre = only_letters("nombre")

            apellido = only_letters("apellido")

            while True:
                correo = input("Correo atleta: ").upper()
                if re.findall(".{1}@", correo) != []:
                    break
                else:
                    print("Correo invalido.")

            while True:
                try:
                    fecha_de_nacimiento = input("Fecha de Nacimiento AAAA-MM-DD  ")
                    fecha_de_nacimiento = datetime.strptime(fecha_de_nacimiento, "%Y-%m-%d").date()
                    break
                except ValueError:
                    print("Fecha invalida.")

            pais_origen = only_letters("pais")

            ciudad_origen = only_letters("ciudad")

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
        # Devolver al menú

'''La función insertar_tabla_atleta() existe para agregar un nuevo atleta a su
    respectiva tabla, de ya existir el número de identificación o número de
    inscripción se le notificará al usuario, de lo contrario creará el atleta
    con la información suministrada. (Nótese que se realizan chequeos de que el
    tipo de información corresponda con lo estipulado en la tabla) '''

def in_db(con_sql, column, attribute, table):
    cursor = con_sql.cursor()
    check = f"SELECT {column} FROM {table} where {column} = '{attribute}'"
    cursor.execute(check)
    return cursor.fetchone()

'''La función in_db() realiza un chequeo de la existencia de un atributo
    especifico, en una tabla y columna específica en la conexión suministrada;
    retornará None si no encuentra ningún elemento con las características antes
    mencionadas. '''

def only_letters(txt_content):
    invalid_txt = True
    while invalid_txt:
      txt = input(f"Introducir {txt_content}: ").upper()
      txt = txt.ljust(12)
      if re.findall('''[`!@#$%^&*()_+\-=\[\]{};':\\"|,.<>\/?~\d]''', txt) != []:
          print(f"{txt_content} invalido/a.".capitalize())
      else:
          invalid_txt = False
    return txt

'''La función only_letters() recibe el contenido de la string que pedirá, una vez
    la reciba revisará si está compuesta únicamente de letras, de encontrar algún
    símbolo o número se le comunicará al usuario y seguirá pidiendo una string 
    hasta que le sea suministrada una válida. '''

def input_is_int(input_content):
    invalid_input = True
    while invalid_input:
        try:
            input_int = int(input(f"Numero de {input_content}: "))
            invalid_input = False
        except ValueError:
            print(f"Numero de {input_content} invalido")
    return input_int

'''La función input_is_int() recibe el contenido de el entero que pedirá, una vez
    lo reciba checará si es un entero, de no serlo lo comunicará al usuario y
    pedirá otro input hasta que le sea suministrado uno válido. '''

def resultado_valido():
    invalid_resultado = True
    while invalid_resultado:
        resultado = input("El resultado del atleta es Retirado'R', "
                          "Descalificado'D' o Finalizado'F'?: ").upper()
        if resultado == "R" or resultado == "D" or resultado == "F":
            invalid_resultado = False
        else:
            print("Indicador del resultado invalido")
    return resultado

'''La función resultado_valido() pedirá una string que representará el resultado
    asociado al atleta, de no ser válida seguirá pidiendo otra hasta que lo sea. '''

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

'''La anterior función consulta la tabla atletas por medio de cursorObj, el 
    usuario ingresa la identificación del atleta, la cual por medio de la cadena 
    de texto cad, la cual contiene el comando SQL que consultará la identificación
    suministrada en la tabla de atleta, nos entregará una lista con la
    información del atleta por medio de la función fetchall, la cual es iterada 
    para ser impresa, caso contrario imprime que no se encontró la información. '''
    
def actualizar_tabla_atleta(con):
    cursorObj = con.cursor()
    no_id_atleta = input("Ingrese identificacion de atleta a consultar: ")
    nombre = only_letters("nombre nuevo")

    apellido = only_letters("apellido nuevo")

    cad = f'''UPDATE atleta set nombre = "{nombre}", apellido = "{apellido}"
          where no_id_atleta like "%{no_id_atleta}%" '''
    cursorObj.execute(cad)
    con.commit()

'''La anterior función actualiza la tabla atleta en el archivo BDSQlLiteEjercicioClase.db 
    por medio del cursorObj, tras ello el usuario ingresa la identificación del
    atleta, la cual entra al script SQL y posterior a ello 
    hace commit para salvaguardar dicha acuatlizacón. '''

def modulo_atleta(con):
    init = True
    while init:
        print("¿Qué deseas hacer?\n"
              "1. Registrar un nuevo atleta.\n"
              "2. Modificar la información de un atleta.\n"
              "3. Consutlar la información de un atleta.\n"
              "4. Volver al menú principal.\n"
              "=========================================\n\n")
        opcion = int(input("Ingresa una opción: "))

        if opcion == 1:
            insertar_tabla_atleta(con)
        elif opcion == 2:
            actualizar_tabla_atleta(con)
        elif opcion == 3:
            consultar_tabla_atletas(con)
        elif opcion == 4:
            init = False
        else:
            print("Ingrese una opción correcta")


def crear_carrera(con):
    cursorObj = con.cursor()
    no_evento = input_is_int("evento")

    if in_db(con, "no_evento", no_evento, "carrera") is None:
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

'''La función crear_carrera() crea una nueva carrera en la tabla carrera luego 
    de verificar que esta no exista. '''

def crear_resultado(con):
    cursorObj = con.cursor()
    no_inscripcion = input_is_int("inscripcion atleta")

    no_evento = input_is_int("evento")

    if in_db(con, "no_inscripcion", no_inscripcion, "atleta") and in_db(con, "no_evento", no_evento,
                                                                        "carrera") is not None:
        posicion = input_is_int("posicion")

        tiempo_empleado = input("Tiempo empleado HH:MM : ")

        indicador_resultado = resultado_valido()

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

'''La función crear_resultado() crea la posición y tiempo empleado por un atleta
    especifico en un evento especifico en la tabla resultado_carrera luego de
    revisar que dicho atleta y evento exista, adicionalmente con el número de 
    identificacion del atleta creará una entrada en la tabla clasificacion_final. '''

def actualizar_resultado(con):
    cursorObj = con.cursor()
    no_inscripcion = input_is_int("inscripcion atleta a actualizar resultado")

    posicion = input_is_int("posicion")

    tiempo_empleado = input("Tiempo empleado HH:MM : ")

    indicador_resultado = resultado_valido()

    cad = f'''UPDATE resultado_carrera set posicion = "{posicion}",
           tiempo_empleado = "{tiempo_empleado}",
           indicador_resultado ="{indicador_resultado}"
           where no_inscripcion like "%{no_inscripcion}%" '''
    cursorObj.execute(cad)
    con.commit()

'''La anterior función actualiza la tabla resultado_carrera en el archivo 
    BDSQlLiteEjercicioClase.db por medio del cursorObj, tras ello el usuario 
    ingresa el número de incripcion del atleta, posición y tiempo empleado los 
    cuales entra al script SQL que cambia los valores ingresados de las tablas
    y posterior a ello hace commit para salvaguardar dicha actualización. '''

def registrar_atletas_descalificados(con):
    cursorObj = con.cursor()
    no_inscripcion = input_is_int("inscripcion atleta a modificar")

    indicador_resultado = resultado_valido()

    cad = f'''UPDATE resultado_carrera set indicador_resultado = "{indicador_resultado}"
          where no_inscripcion like "%{no_inscripcion}%" '''
    cursorObj.execute(cad)
    con.commit()
'''La anterior función actualiza la tabla resultado_carrera en el archivo 
    BDSQlLiteEjercicioClase.db por medio del cursorObj, tras ello el usuario 
    ingresa el número de incripcion del atleta la cual entra al script SQL que 
    actualiza valor de indicador resultado en la tabla y posterior a ello hace
    commit para salvaguardar dicha actualización. '''

def consultar_clasificacion(con):
    cursorObj = con.cursor()
    no_evento = input_is_int("evento")

    cursorObj.execute(f"SELECT * FROM clasificacion_final WHERE no_evento = {no_evento} ORDER BY tiempo_empleado ASC")
    lista = cursorObj.fetchall()
    print(lista)

    if not lista:
        print("No se encontraron resultados.")

'''La anterior función consulta la tabla clasificacion_final por medio del cursorObj, el 
    usuario ingresa el número de carrera, la cual entra a la cadena de texto 
    que el cursorObj ejecuta el comando SQL que consultará los atletas que 
    particioparon en la carrera, cuya información se encuentra la tabla de 
    clasificacion_final, nos entregará una lista con la
    información del atleta por medio de la función fetchall, la cual es impresa  
    por orden de tiempo empleado, caso contrario imprime que no se encontró la información. '''

def main_menu(con):
    init = True

    print("MEDIA MARATÓN DE BOGOTÁ: \n"
          "============================================\n")
    while init:
        pass
        print(
              "¿Qué operación desea realizar?\n"
              "1. Habilitar una nueva carrera.\n"
              "2. Registrar/ Modificar/ Consultar atleta.\n"
              "3. Generar resultado de carrera.\n"
              "4. Gestionar descalificados.\n"
              "5. Consultar el resultado de una carrera.\n"
              "6. Terminar sesión.\n\n")

        try:
            option = int(input("Ingresa una opción: "))

            if option == 1:
                crear_carrera(con)

            elif option == 2:
                modulo_atleta(con)

            elif option == 3:
                actualizar_resultado(con)

            elif option == 4:
                registrar_atletas_descalificados(con)

            elif option == 5:
                consultar_clasificacion(con)

            elif option == 6:
                print("Hasta luego.")
                init = False

            else:
                print("Opción inválida, intente de nuevo: ")

        except ValueError:
            print("Opción inválida, intente de nuevo: ")


def main():
    con = conexion_sql()
    tabla_atleta(con)
    tabla_carrera(con)
    tabla_resultado_carrera(con)
    tabla_clasificacion_final(con)
    main_menu(con)
    con.close()


main()