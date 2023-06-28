
## Diseño: 

En el siguiente diagrama se muestran las clases que tiene el programa y las relaciones que tienen todas las clases entre sí:

![Diagrama de clases](https://github.com/Camgamez/MediaMaraton/blob/master/Media%20marat%C3%B3n%20BTA.png)

Ya que estamos administrando la Media Maraton de Bogotá, tenemos que pensar en diferentes aspectos de este importante evento para la ciudad. En primer lugar debemos pensar que vamos a realizar diferentes carreras, donde van a participar diferentes atletas. Toda carrera contiene una clasificación, y así mismo todo atleta tiene una clasificación para cada carrera. De manera análoga a la anterior, toda carrera contiene un resultado y todos los atletas tienen un resultado en cada carrera. 

## Manual técnico: 

En el momento, el manuál técnico del programa se encuentra como [anotaciones al código](https://github.com/Camgamez/MediaMaraton/blob/master/media_maraton.py).
---

## Casos de uso:

### Actores: 
En el presente programa solo existe un actor con permisos para acceder al sistema, ingresar, eliminar y/o actualizar cualquier información.


---
### Módulo Inicial:

#### Descripción:
El módulo inicial hace las veces de menú principal, es decir que en este módulo se van a presentar las opciones de selección de los siguientes módulos y dependiendo de la opción seleccionada por el usuario, lo dirige al módulo apropiado.

#### Pre-requisitos:
NA

#### Flujo principal: 
Tras iniciar el programa, el sistema le presentará al usuario un menú con las siguientes opciones:
1. Habilitar una nueva carrera.
2. Ingresar al modulo Atletas. 
3. Generar resultado de carrera.
4. Actualizar resultado. 
5. Gestionar clasificaciones.
6. Consultar el resultado. 
7. Cerrar Sesión. 

#### Flujo Alternativo: 
Na
#### Puntos de extensión:

Dependiendo de la opción seleccionada por el usuario, el sistema lo re-dirige al módulo correspondiente.
---
### Módulo para habilitar una carrera:

#### Descripción: 
Este módulo permite crear una carrera, consultando al usuario los datos básicos de la misma como lo son el número del evento, el año de realización y los premios del primer al tercer puesto. 

#### Prerrequisitos: 
Na

#### Flujo Principal: 
Luego de ingresar a este módulo, el programa consulta por la siguiente información en un formulario:
- Número del evento.
- Año de realización.
- Primer Premio.
- Segundo Premio.
- Tercer Premio.
Después de que el usuario ingrese la información en el formulario, se le indica que haga clic en “Crear Carrera”. 

Aquí es sistema realiza una verificación de la integridad de los datos y la unicidad del número de evento. 

#### Flujo Alternativo:
1. En caso de que una carrera con el numero de evento especificado ya exista, el sistema informa al usuario sobre esta situación y solicita que se ingrese de nuevo la información.
2. En caso que el valor ingresado para el numero de carrera no sea un número, es sistema vuekve a solicitar la información. 

#### Post-Condiciones: 
En caso de exito al registrar la carrera, esta debe verse reflejada en la basde de datos.

---
### Módulo Atletas:

#### Descripción:
Este módulo es un menú intermedio entre el menú principal y la opción de registrar, modificar o consultar la información de un atleta.

#### Pre-requisitos:
El usuario debe haber seleccionado la opción "Atletas" del menú principal. 

#### Flujo principal: 
Al ingresar en este módulo, esl usuario es presentado con 4 opciones:
- Registrar atleta. 
- Modificar atleta. 
- Consultar atleta.
- Volver

Dependiendo de la opción seleccionada, es usuario puede navegar entre los diferentes módulos mencionados.

#### Flujo Alternativo:
+ Modificar Atleta: Si al consultar en la base de datos, el id atleta no existe, consulta al usuario si desea agregar un nuevo atleta utilizando este id. 
+ Consultar Atleta: Si al verificar en la base de datos la existencia del id atleta, no encuentra ninguna coincidencia, el sistema consulta al usuario si desea agregarlo. 

#### Post-condiciones:
Al terminar este flujo, la base de datos debe quedar actualizada con la información de los atletas agregados y modificados. 
---
### Módulo Registro Atletas:
#### Descripción:
En este módulo, es sitema recive la información de cada nuevo atleta registrado. 

#### Prerequisitos:
Na

#### Flujo Principal:

El sistema solicita la siguiente información: 
  - id atleta.
  - id inscripción
  - nombre.
  - apellido.
  - fecha de nacimiento.
  - país.
  - ciudad.

Luego que el usuario digite la información, al hacer click en el botón "registrar", es sistema verifica la integridad de los datos y la unicidad del id Atleta, si la información pasa ambos filtros, el nuevo atleta queda regustrado. 

#### Flujo Alternativo:
+ En caso de que la información ingresada no pase la verificación (quizá el valor de la fecha no tiene el formato correcto, o el correo ingresado no es valido) el sistena informal cliente que la información ingresada no es apropiada y la solicita de nuevo. 
+ En caso de que el id atleta ya exista en la base de datos, el sistema informa al usuario sobre esta situación y solicita que se ingrese de nuevo la información.

#### Postcondiciones:

La base de datos tiene un nuevo atleta registrado. 
---
### Modulo Modificar Atleta:
#### Descripción:
Este módulo permite corregir el nombre y apellido de un atleta. 

#### Flujo Principal

Al iniciar este modulo, el sistema solicita al usuario un id atleta y confirma la existencia de esta información en la base de datos. Una vez encontrado el atleta, el sistema solicita al usuario que ingrese el nuevo nombre y apellido del atleta. 

Luego de verificada la integridad de la información, el sistema actualiza el nombre y apellido del usuario en la base de datos.

#### Flujo Alternativo:
1. Si el id atleta ingresado ni existe en la base de atos, el sistema le informa esto al cliente y solicita una nueva id. 

2. Si el nombre contiene números o caracteres especialez, el sistema le informa al usuario que estos no son valjdos y solicita de nuevo la información. 

#### Post Condiciones:

La en nombre y apellido del atleta son actualizados por la información nueva. 
---
### Modulo Consultar Atleta:

#### Descripción:
En este módulo permite realizar la consulta de 

#### Prerequisitos:
Deben existir entradas en la base de datos de los atletas.

#### Flujo Principal:

El sistema solicita al usuario por el id atleta que desea consultar. Tras recibir la información, se consulta en la base de datos por el identificador y retorna la información del atleta consultado. 

#### Flujo Alternativo:

Si el id atleta ingresado en el sistema no existe, entonces el programa solicita un nuevo ID atleta. 

#### Post Condiciones:
Na

---
### Módulo para generar el resultado carrera:

#### Descripción:
El objetivo de este módulo es gestionar el resultado de determinada carrera, relacionando el número del evento, el número de carrera.el id atleta, el tiempo empleado por el atleta para terminar la carrera, su posición y un indicador del estado del atleta (descalificado, retirado, finalizó). 

#### Pre-requisitos:
Debe existir una lista de atletas y al menos una carrera.

#### Flujo principal: 
Después de ingresar a este módulo, el sistema primero consulta al usuario por la edición de la carrera sobre la que desea trabajar. 

Una vez que el usuario escoge la carrera que desea editar, el sistema pregunta por el id atleta que desea ingresar. Si el atleta no está en la tabla, el sistema solicita que se ingrese en tiempo empleado y el indicador de finalización de carrera.

#### Flujo Alternativo: 
En caso que el id atleta ingresado por el usuario ya exista en la base de datos, el programa va a mostrar la información del atleta en cuestión y posteriormente va a consultar al usuario si desea modificar información del atleta respecto a la carrera o si desea ingresar la información de un nuevo atleta.
Si la información se ingresó de manera incompleta o de manera incorrecta, el sistema informa por medio de un mensaje el problema y regresa a la solicitud actual.

#### Post-condiciones:
En la tabla de resultados, debe quedar registrado el resultado de todos los atletas que compitieron en determinada carrera junto con el tiempo empleado para ello, además la información del tiempo ayudará a organizar cuáles son los puestos en que cada atleta queda al terminar la maratón. 

#### Puntos de extensión:
El usuario también puede seleccionar una opción adicional para volver al menú anterior.


---
### Módulo de gestión de descalificados:

#### Descripción:
Este módulo permite realizar consultas del resultado final de una carrera, mostrando la información de los atletas: id, nombre, apellido, fecha de nacimiento, país y ciudad de origen y tiempo de finalización. 

#### Pre-requisitos:
En el sistema tiene que existir al menos una carrera y una clasificación de la misma.

#### Flujo principal: 
Tras seleccionar la opción para acceder a este módulo, se le solicita al usuario que ingrese el número de identificación, si el número este coincide con algún atleta registrado, a continuación el sistema requiere que el usuario ingrese el número de la carrera en la que sucedió el evento y por último se le pide al usuario que ingrese el estado del atleta donde existen tres opciones: 
- R = Retirado.
- F = Finalizado.
- D = Descalificado.

#### Flujo Alternativo: 
En caso de que el número de identificación ingresado por el atleta no tenga ninguna coincidencia en el sistema, se emite una notificación mencionando que no se encontraron coincidencias en la base de datos y solicitando que se ingrese un nuevo número de identificación.
Por otro lado, si el número de carrera no tiene coincidencias en el sistema, se le informa al usuario de esta situación y se le pregunta por un nuevo número.

#### Post-condiciones:
El indicador de clasificación del usuario debe quedar actualizado después de este flujo. 

#### Puntos de extensión:
El usuario también puede seleccionar una opción adicional para volver al menú anterior.


---
### Módulo de consulta resultado carrera:

#### Descripción:
Este módulo permite al usuario consultar cuál fué el resultado en particular de una carrera.

#### Pre-requisitos:
Es necesario que exista el resultado de al menos una carrera en el sistema. 

#### Flujo principal: 
Tras ingresar al módulo, el sistema le solicita al usuario que ingrese el número de carrera sobre la que desea conocer el resultado. Si encuentra una coincidencia, le presenta al usuario una tabla con la siguiente información:
- id atleta.
- Nombre.
- Apellido.
- Tiempo empleado.
- País de origen.
- Ciudad de origen.
- Fecha de nacimiento.
La tabla permite al usuario clicar en el campo sobre el cuál desea organizar la información.

#### Flujo Alternativo: 
Suponiendo que el usuario ingresa un número de carrera que no existe en el inicio de la consulta, el sistema muestra una notificación al respecto y solicita al usuario ingresar un valor diferente.

#### Post-condiciones:
na
#### Puntos de extensión:
El módulo tiene una opción para volver al menú principal.
