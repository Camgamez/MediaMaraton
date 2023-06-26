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
        con = sqlite3.connect('../BDSQlLiteEjercicioClase.db')
        return con
    except Error:
        print(Error)

'''El anterior método se encarga de la creación del cursor encargado de recorrer
    la tabla, además archivo de la base de datos si este no existe, sí ya existe
    se conecta a dicho archivo. Dado el caso que no se de ninguno 
    de los casos presentados imprime en pantalla el error. '''

def tabla_atleta(con): #Creación de la tabla atleta sí no existe, sino sigue.
    cursorObj = con.cursor()
    cursorObj.execute('''CREATE TABLE IF NOT EXISTS atleta(
                          no_id_atleta text,
                          no_inscripcion INTEGER,
                          nombre text, 
                          apellido text, 
                          correo text, 
                          fecha_de_nacimiento date,
                          pais_origen, 
                          ciudad_origen, 
                          PRIMARY KEY(no_id_atleta,no_inscripcion))
                          ''')  # Tabla falta foto
    con.commit()

'''El anterior método crea la tabla atleta en el archivo BDSQlLiteEjercicioClase.db
    por medio del cursorObj el cual ejecuta el comando SQL y posterior a ello hace
    commit para salvaguardar dicha creación, dado el caso que exista la tabla, la
    método no realiza nada. '''

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

'''El anterior método crea la tabla carrera en el archivo BDSQlLiteEjercicioClase.db
    por medio del cursorObj el cual ejecuta el comando SQL y posterior a ello hace
    commit para salvaguardar dicha creación, dado el caso que exista la tabla, la
    método no realiza nada. '''

def tabla_resultado_carrera(con): #Creación de la tabla resultado carrera si no existe, sino sigue.
    if con is not None:
        cursorObj = con.cursor()
        cursorObj.execute('''CREATE TABLE IF NOT EXISTS resultado_carrera(
                        no_evento integer,
                        no_id_atleta text, 
                        posicion integer,
                        tiempo_empleado TIME CHECK(tiempo_empleado LIKE '__:__'),
                        indicador_resultado char(1),
                        PRIMARY KEY(no_evento,no_id_atleta))''')
        con.commit()

'''El anterior método crea la tabla resultado carrera en el archivo 
    BDSQlLiteEjercicioClase.db por medio del cursorObj el cual ejecuta el comando 
    SQL y posterior a ello hace commit para salvaguardar dicha creación, dado el 
    caso que exista la tabla, la método no realiza nada. '''

def tabla_clasificacion_final(con): #Creación de la tabla clasificación final si no existe, sino sigue.
    cursorObj = con.cursor()
    cursorObj.execute('''CREATE TABLE IF NOT EXISTS clasificacion_final(
                          no_id_atleta text PRIMARY KEY,
                          no_evento INTEGER,
                          nombre text, 
                          apellido text, 
                          fecha_de_nacimiento date,
                          pais_origen text, 
                          ciudad_origen text, 
                          tiempo_empleado TIME 
                          )''')  # Tabla falta foto
    con.commit()

'''El anterior método crea la tabla clasificación final en el archivo 
    BDSQlLiteEjercicioClase.db por medio del cursorObj el cual ejecuta el comando 
    SQL y posterior a ello hace commit para salvaguardar dicha creación, dado el 
    caso que exista la tabla, el método no realiza nada. '''

class Revisor:

    def in_db(con_sql, column, attribute, table):
        cursor = con_sql.cursor()
        check = f"SELECT {column} FROM {table} where {column} = '{attribute}'"
        cursor.execute(check)
        return cursor.fetchone()

    '''El método in_db() realiza un chequeo de la existencia de un atributo
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

    '''El método only_letters() recibe el contenido de la string que pedirá, una vez
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

    '''El método input_is_int() recibe el contenido de el entero que pedirá, una vez
        lo reciba checará si es un entero, de no serlo lo comunicará al usuario y
        pedirá otro input hasta que le sea suministrado uno válido. '''

class Clasificacion (Revisor):

    def __init__(self):
        self.__no_evento = None

    def set_evento(self, num_evento):
        self.__no_evento = num_evento

    def get_evento(self):
        return self.__no_evento

    def gen_list_clasif(self, sql_query, cursorObj):
        print(sql_query)
        cursorObj.execute(sql_query)
        list = cursorObj.fetchall()
        print(list)
        if not list:
            print(f"No se encontraron resultados asociados al evento {self.get_evento}.")
    #Comentar

    def consultar_clasificacion(self, con, num_evento, option):
        cursorObj = con.cursor()
        self.set_evento(num_evento)
        try:
            if option == 1:
                sql_query = f"SELECT * FROM clasificacion_final WHERE no_evento = {self.get_evento()} ORDER BY tiempo_empleado ASC"
                self.gen_list_clasif(sql_query, cursorObj)
            elif option == 2:
                sql_query = f"SELECT * FROM clasificacion_final WHERE no_evento = {self.get_evento()} ORDER BY nombre ASC"
                self.gen_list_clasif(sql_query, cursorObj)
            elif option == 3:
                sql_query = f"SELECT * FROM clasificacion_final WHERE no_evento = {self.get_evento()} ORDER BY apellido ASC"
                self.gen_list_clasif(sql_query, cursorObj)
            elif option == 4:
                sql_query = f"SELECT * FROM clasificacion_final WHERE no_evento = {self.get_evento()} ORDER BY fecha_de_nacimiento ASC"
                self.gen_list_clasif(sql_query, cursorObj)
            elif option == 5:
                sql_query = f"SELECT * FROM clasificacion_final WHERE no_evento = {self.get_evento()} ORDER BY pais_origen ASC"
                self.gen_list_clasif(sql_query, cursorObj)
            elif option == 6:
                sql_query = f"SELECT * FROM clasificacion_final WHERE no_evento = {self.get_evento()} ORDER BY ciudad_origen ASC"
                self.gen_list_clasif(sql_query, cursorObj)
            else:
                print("Opción inválida, intente de nuevo.")
        except ValueError:
            print("Opción inválida, intente de nuevo.")

    '''El anterior método consulta la tabla clasificacion_final por medio del cursorObj, el 
            usuario ingresa el número de evento a buscar a través del cursorObj, la secuencia
            Sql consultará los atletas que participaron en dicho evento, información que se
            encuentra en la tabla de clasificacion_final, guardaremos dicha información en una
            lista gracias a fetchall(); lista que finalmente imprimiremos ordenada por tiempo
            empleado, de no existir estos resultados imprimimos que no se encontró la información. '''

class Resultado(Revisor):

    def __init__(self):
        self.__posicion = None
        self.__tiempo = None
        self.__indicador = None
        self.__no_id_atleta = None
        self.__no_evento = None

    def set_posicion(self):
        self.__posicion = Revisor.input_is_int("posicion")

    def set_tiempo(self):
        # re.search("\d{2}:\d{2}", input("Tiempo empleado HH:MM : "))
        t_e = input("Tiempo empleado HH:MM : ")
        self.__tiempo = t_e

    def set_indicador(self):
        invalid_resultado = True
        while invalid_resultado:
            resultado = input("El resultado del atleta es Retirado'R', "
                            "Descalificado'D' o Finalizado'F'?: ").upper()
            if resultado == "R" or resultado == "D" or resultado == "F":
                self.__indicador = resultado
                invalid_resultado = False
            else:
                print("Indicador del resultado invalido")
    '''El método set_indicador() pedirá una string que representará el resultado
    asociado al atleta, de no ser válida seguirá pidiendo otra hasta que lo sea. '''
    def set_id(self):
        self.__no_id_atleta = Revisor.input_is_int("documento atleta")

    def set_evento (self):
        self.__no_evento = Revisor.input_is_int("evento")

    def get_posicion(self):
        return self.__posicion

    def get_tiempo(self):
        return self.__tiempo

    def get_indicador(self):
        return self.__indicador

    def get_id(self):
        return self.__no_id_atleta
    def get_evento(self):
        return self.__no_evento


    def crear_resultado(self, con):
        cursorObj = con.cursor()
        self.set_id()
        self.set_evento()
        if Revisor.in_db(con,
                         "no_evento",
                         self.get_evento(),
                         "carrera") and Revisor.in_db(con,
                                                      "no_id_atleta",
                                                      self.get_id(),
                                                      "atleta") is not None:
            self.set_posicion()
            self.set_tiempo()

            self.set_indicador()
            cad = f'''INSERT INTO resultado_carrera VALUES(
                    '{self.get_evento()}',
                    '{self.get_id()}',
                    '{self.get_posicion()}',
                    '{self.get_tiempo()}',
                    '{self.get_indicador()}'
                )'''
            cad2 = f'''SELECT * FROM atleta where no_id_atleta like "%{self.get_id()}%" '''
            cursorObj.execute(cad2)
            lista = cursorObj.fetchall()
            for row in lista:
                nombre = row[2]
                apellido = row[3]
                fecha_de_nacimiento = row[5]
                pais_origen = row[6]
                ciudad_origen = row[7]
            cad3 = f'''INSERT INTO clasificacion_final VALUES(
                    '{self.get_id()}',
                    '{self.get_evento()}',
                    '{nombre}',
                    '{apellido}',
                    '{fecha_de_nacimiento}',
                    '{pais_origen}',
                    '{ciudad_origen}',
                    '{self.get_tiempo()}'
                    )'''
            try:
                cursorObj.execute(cad)
            except sqlite3.IntegrityError:
                print(f"'{self.get_tiempo()}' no es un tiempo valido.")
                return
            cursorObj.execute(cad3)
            con.commit()

        else:
            print(f"El evento {self.get_evento} y/o el atleta identificado con {self.get_id} no existe.")
    '''El método crear_resultado() guarda la posición y tiempo empleado por un atleta
    especifico en un evento especifico en la tabla resultado_carrera luego de
    revisar que dicho atleta y evento exista, adicionalmente con el número de 
    identificacion del atleta creará una entrada en la tabla clasificacion_final. '''


    def registrar_atletas_descalificados(self, con):
        cursorObj = con.cursor()
        self.set_id()

        self.set_indicador()

        cad = f'''UPDATE resultado_carrera set indicador_resultado = "{self.get_indicador()}"
                where no_id_atleta like "%{self.get_id()}%" '''
        cursorObj.execute(cad)
        con.commit()
        '''El anterior método actualiza la tabla resultado_carrera en el archivo 
            BDSQlLiteEjercicioClase.db por medio del cursorObj, tras ello el usuario 
            ingresa el número de incripcion del atleta el cual actualizará el indicador
            del estado del atleta en la tabla, posterior a esto se realiza un
            commit para salvaguardar dicha actualización. '''

    def actualizar_resultado(self, con):
        cursorObj = con.cursor()
        # Checar existencia de resultado
        self.set_evento()
        if Revisor.in_db(con, "no_evento", self.get_evento(), "resultado_carrera") == None:
            print(f"No existe un resultado relacionado al evento {self.get_evento()}.")
            return

        self.set_id()
        self.set_posicion()
        self.set_tiempo()
        self.set_indicador()

        cad = f'''UPDATE resultado_carrera set posicion = "{self.get_posicion()}",
            tiempo_empleado = "{self.get_tiempo()}",
            indicador_resultado ="{self.get_indicador()}"
            where no_id_atleta like "%{self.get_id()}%" and no_evento like "%{self.get_evento()}%"'''
        cad2=f'''UPDATE clasificacion_final set tiempo_empleado ="{self.get_tiempo()}" where no_id_atleta like "%{self.get_id()}%" '''
        cursorObj.execute(cad)
        cursorObj.execute(cad2)
        con.commit()
    '''El anterior método actualiza la tabla resultado_carrera en el archivo 
        BDSQlLiteEjercicioClase.db por medio del cursorObj, tras ello el usuario 
        ingresa el número de incripcion del atleta, posición y tiempo empleado los 
        cuales entra al script SQL que cambia los valores ingresados de las tablas
        y posterior a ello hace commit para salvaguardar dicha actualización. '''

class Carrera (Revisor):

    def __init__(self):
        self.__no_evento = None
        self.__year = None
        self.__primer_premio = None
        self.__segundo_premio = None
        self.__tercer_premio = None

    '''Los siguientes 5 métodos son los setters '''
    def set_evento (self):
        self.__no_evento = Revisor.input_is_int("numero del evento")

    def set_year(self):
        self.__year = Revisor.input_is_int("año del evento")

    def set_primer(self):
        premio_primer_puesto = input("Premio primer puesto: ").upper()
        self.__primer_premio = premio_primer_puesto.ljust(12)

    def set_segundo(self):
        premio_segundo_puesto = input("Premio segundo puesto: ").upper()
        self.__segundo_premio = premio_segundo_puesto.ljust(12)

    def set_tercer(self):
        premio_tercer_puesto = input("Premio tercer puesto: ").upper()
        self.__tercer_premio = premio_tercer_puesto.ljust(12)

    '''Los siguientes 5 métodos son los getters de las propiedades de la carrera.'''
    def get_evento(self):
        return self.__no_evento

    def get_year(self):
        return self.__year

    def get_primer(self):
        return self.__primer_premio

    def get_segundo(self):
        return self.__segundo_premio

    def get_tercer(self):
        return self.__tercer_premio

    def crear_carrera(self, con):
        cursorObj = con.cursor()
        self.set_evento()

        if Revisor.in_db(con, "no_evento", self.get_evento, "carrera") is None:
            self.set_year()
            self.set_primer()
            self.set_segundo()
            self.set_tercer()

            cad = f'''INSERT INTO carrera VALUES(
                    '{self.get_evento()}',
                    '{self.get_year()}',
                    '{self.get_primer()}',
                    '{self.get_segundo()}',
                    '{self.get_tercer()}'
                )'''

            cursorObj.execute(cad)
            con.commit()
        else:
            print(f"El número evento ya existe {self.get_evento}.")

    '''El método crear_carrera() crea una nueva carrera en la tabla carrera luego 
        de verificar que esta no exista. '''

class Atleta (Revisor):

    def __init__(self):
        self.__no_id_atleta = None
        self.__no_inscripcion = None
        self.__nombre = None
        self.__apellido = None
        self.__correo = None
        self.__fecha_de_nacimiento = None
        self.__pais_origen = None
        self.__ciudad_origen = None

    def set_id(self):
        # Hace que la propiedad no_id_atleta sea igual a un valor de 12 dígitos/ caracteres
        self.__no_id_atleta = input("Ingrese el documento del atleta: ")

    def set_no_inscripcion (self):
        # Verifica que el valor ingresado sea un número y lo ingresa como propiedad no_inscripcion.
        # En caso contrario lo sigue preguntanto.
        self.__no_inscripcion = Revisor.input_is_int("inscripcion atleta")

    # Las siguientes son los métodos de los setters, estas van a asegurar que la información ingresada sea apropiada.
    def set_nombre(self):
        self.__nombre = Revisor.only_letters("nombre")

    def set_apellido(self):
        self.__apellido = Revisor.only_letters("apellido")

    def set_correo(self):
        init = True
        while init:
            correo = input("Correo atleta: ").upper()
            if re.findall(".{1}@", correo):
                self.__correo = correo
                init = False
            else:
                print("Correo invalido.")

    def set_cumple(self):
        init = True
        while init:
            try:
                fecha_de_nacimiento = input("Fecha de Nacimiento AAAA-MM-DD  ")
                self.__fecha_de_nacimiento = datetime.strptime(fecha_de_nacimiento, "%Y-%m-%d").date()
                init = False
            except ValueError:
                print("Fecha invalida.")

    def set_pais(self):
        self.__pais_origen = Revisor.only_letters("pais")

    def set_ciudad(self):
        self.__ciudad_origen = Revisor.only_letters("ciudad")

    # son los getters
    def get_id(self):
        return self.__no_id_atleta

    def get_inscripcion(self):
        return self.__no_inscripcion

    def get_nombre(self):
        return self.__nombre

    def get_apellido(self):
        return self.__apellido

    def get_correo(self):
        return self.__correo

    def get_cumple(self):
        return self.__fecha_de_nacimiento

    def get_pais(self):
        return self.__pais_origen

    def get_ciudad(self):
        return self.__ciudad_origen

    def insertar_tabla_atleta(self, con):
        cursorObj = con.cursor()
        init = True

        while init:
            self.set_id()

            if Revisor.in_db(con, "no_id_atleta", self.get_id(), "atleta"):

                print("El documento de identificación que ingresaste ya existe\n"
                      "Por favor intenta con otro.")
            else:

                self.set_no_inscripcion()
                self.set_nombre()
                self.set_apellido()
                self.set_correo()
                self.set_cumple()
                self.set_pais()
                self.set_ciudad()

                cad = f'''INSERT INTO atleta VALUES(
                '{self.get_id()}',
                '{self.get_inscripcion()}',
                '{self.get_nombre()}',
                '{self.get_apellido()}',
                '{self.get_correo()}',
                '{self.get_cumple()}',
                '{self.get_pais()}',
                '{self.get_ciudad()}'
                )'''
                cursorObj.execute(cad)
                con.commit()

                init = False
    '''El método insertar_tabla_atleta() existe para agregar un nuevo atleta a su
        respectiva tabla, de ya existir el número de identificación o número de
        inscripción se le notificará al usuario, de lo contrario creará el atleta
        con la información suministrada. (Nótese que se realizan chequeos de que el
        tipo de información corresponda con lo estipulado en la tabla) '''
    def actualizar_tabla_atleta(self, con):
        cursorObj = con.cursor()
        self.set_id()
        if Revisor.in_db(con, "no_id_atleta", self.get_id(), "atleta") != None:
            nombre = Revisor.only_letters("nombre nuevo")

            apellido = Revisor.only_letters("apellido nuevo")

            cad = f'''UPDATE atleta set nombre = "{nombre}", apellido = "{apellido}"
                where no_id_atleta like "%{self.get_id()}%" '''
            cursorObj.execute(cad)
            con.commit()
        else:
            print(f"Atleta con numero de identificacion {self.get_id()} no existe.")

    '''El anterior método actualiza la tabla atleta en el archivo BDSQlLiteEjercicioClase.db 
        por medio del cursorObj, tras ello el usuario ingresa la identificación del
        atleta, la cual entra al script SQL y posterior a ello 
        hace commit para salvaguardar dicha acuatlizacón. '''

    def consultar_tabla_atletas(self, con):
        cursorObj = con.cursor()
        id_consultada = input("Ingrese su documento de identificacion: ")
        cad = f'''SELECT * FROM atleta where no_id_atleta like "%{id_consultada}%" '''
        cursorObj.execute(cad)
        lista = cursorObj.fetchall()
        print(lista)
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
            print(f"No se encontro el atleta con identificacion {id_consultada}.")

    '''El anterior método consulta la tabla atletas por medio de cursorObj, el 
    usuario ingresa la identificación del atleta, la cual por medio de la cadena 
    de texto cad, la cual contiene el comando SQL que consultará la identificación
    suministrada en la tabla de atleta, nos entregará una lista con la
    información del atleta por medio de el método fetchall, la cual es iterada 
    para ser impresa, caso contrario imprime que no se encontró la información. '''


    def modulo_atleta(self, con):
        init = True
        while init:
            print("¿Qué deseas hacer?\n"
                "1. Registrar un nuevo atleta.\n"
                "2. Modificar la información de un atleta.\n"
                "3. Consultar la información de un atleta.\n"
                "4. Volver al menú principal.\n"
                "=========================================\n\n")
            opcion = int(input("Ingresa una opción: "))

            if opcion == 1:
                self.insertar_tabla_atleta(con)
            elif opcion == 2:
                self.actualizar_tabla_atleta(con)
            elif opcion == 3:
                self.consultar_tabla_atletas(con)
            elif opcion == 4:
                init = False
            else:
                print("Ingrese una opción válida")
    """ El método modulo_atleta genera un menu de seleccion en que el usuario puede escoger si desea
    ingresar, modificar o consultar la informacion de un atleta en particular."""

def main_menu(con, atleta, carrera, resultado, clasificacion):
    # Método detallada en el flujo principal del caso de uso "Módulo registro atletas en la base de datos
    init = True # Banderilla

    print("MEDIA MARATÓN DE BOGOTÁ: \n"
          "============================================\n")
    while init:
        pass
        print(
              "¿Qué operación desea realizar?\n"
              "1. Habilitar una nueva carrera.\n"
              "2. Registrar/ Modificar/ Consultar atleta.\n"
              "3. Generar resultado de carrera.\n"
              "4. Actualizar resultado carrera.\n"
              "5. Gestionar descalificados.\n"
              "6. Consultar el resultado de una carrera.\n"
              "7. Terminar sesión.\n\n")

        try:
            option = int(input("Ingresa una opción: "))

            if option == 1:
                carrera.crear_carrera(con)

            elif option == 2:
                atleta.modulo_atleta(con)

            elif option == 3:
                resultado.crear_resultado(con)

            elif option == 4:
                resultado.actualizar_resultado(con)

            elif option == 5:
                resultado.registrar_atletas_descalificados(con)

            elif option == 6:
                clasificacion.consultar_clasificacion(con)

            elif option == 7:
                print("Hasta luego.")
                init = False # termina el ciclo

            else:
                print("Opción inválida, intente de nuevo: ")

        except ValueError:
            print("Opción inválida, intente de nuevo: ")

def crearSQLTables(con):
    tabla_atleta(con)
    tabla_carrera(con)
    tabla_resultado_carrera(con)
    tabla_clasificacion_final(con)

def main():
    con = conexion_sql()
    atleta = Atleta()
    carrera = Carrera()
    resultado = Resultado()
    clasificacion = Clasificacion()
    crearSQLTables(con)
    main_menu(con, atleta, carrera, resultado, clasificacion)
    con.close()

#main()