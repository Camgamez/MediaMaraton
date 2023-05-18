# Entrega Proyecto: 

## Diseño: 

En el siguiente diagrama se muestran las clases que tiene el programa y las relaciones que tienen todas las clases entre sí:

![Diagrama de clases](https://github.com/Camgamez/MediaMaraton/blob/master/Media%20marat%C3%B3n%20BTA%20(1).png)

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
2. Registrar/ Modificar/ Consultar atleta.
3. Generar resultado de carrera.
4. Gestionar descalificados.
5. Consultar el resultado de una carrera.

#### Flujo Alternativo: 
NA
#### Puntos de extensión:
Dependiendo de la opción seleccionada por el usuario, el sistema lo re-dirige al módulo correspondiente.

### Módulo para habilitar una carrera:

#### Descripción: 
Este módulo permite crear una carrera, consultando al estudiante los datos básicos de la misma como lo son el número del evento, el año de realización y los premios del primer al tercer puesto. 

#### Prerrequisitos: 
El modelo no es claro sobre si este rol necesita autenticación. Se debe seleccionar una opción del menú principal.
Debe existir una base de datos de las carreras. 

#### Flujo Principal: 
Luego de ingresar a este módulo, el programa consulta por la siguiente información en un formulario:
- Número del evento.
- Año de realización.
- Primer Premio.
- Segundo Premio.
- Tercer Premio.
Después de que el usuario ingrese la información en el formulario, se le indica que haga clic en “Crear Carrera”. 

#### Flujo Alternativo:
Na.

#### Post-Condiciones: 
Una nueva carrera debe quedar registrada en la base de datos de las carreras.
Puntos de extensión:
El usuario también puede seleccionar una opción adicional para volver al menú anterior.


---
### Módulo de registro de atletas en la base de datos: 

#### Descripción:
Este módulo permite registrar, modificar y consultar la información de los atletas que desean participar en la competencia.

#### Pre-requisitos:
El usuario debe haber seleccionado la opción de Agregar/Modificar/Consultar atleta. 

#### Flujo principal: 
Una vez seleccionada esta opción, el sistema le consulta al usuario si desea agregar, modificar o consultar un atleta. 

+ Si el usuario selecciona la opción “Agregar atleta”, solicita la siguiente información: 
  - id atleta.
  - id inscripción
  - nombre.
  - apellido.
  - fecha de nacimiento.
  - país.
  - ciudad.
  - foto.
+ En caso que el usuario seleccione la opción “Modificar atleta”, el sistema solicita al usuario por el id atleta que desea modificar, una vez ingresada esta información el sistema solicita el nuevo nombre y apellido, posteriormente actualiza estos datos en la base de datos.

+ Por otro lado, en caso que la opción escogida sea “Consultar atleta”, el sistema solicita al usuario por el id atleta que desea consultar. Tras recibir la información, se consulta en la base de datos por el identificador y retorna la información del atleta consultado. 

#### Flujo Alternativo: 
+ Agregar Atleta: En caso que el usuario haya seleccionado esta opción, tras consultar en la base de datos, si el usuario existe le ofrece un menú al usuario preguntando si desea consultar o modificar la información. Dependiendo de la opción del usuario, procede a esa parte del flujo. 
+ Modificar Atleta: Si al consultar en la base de datos, el id atleta no existe, consulta al usuario si desea agregar un nuevo atleta utilizando este id. 
+ Consultar Atleta: Si al verificar en la base de datos la existencia del id atleta, no encuentra ninguna coincidencia, el sistema consulta al usuario si desea agregarlo. 

#### Post-condiciones:
Al terminar este flujo, la base de datos debe quedar actualizada con la información de los atletas agregados y modificados. 
Puntos de extensión:
El usuario también puede seleccionar una opción adicional para volver al menú anterior.


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
