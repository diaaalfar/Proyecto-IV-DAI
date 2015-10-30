# Proyecto-IV-DAI
# *Scrumpy*
Jesús Prieto López

[![Build Status](https://travis-ci.org/JesGor/Proyecto-IV-DAI.svg?branch=master)](https://travis-ci.org/JesGor/Proyecto-IV-DAI)

Repositorio dedicado al proyecto de las asignaturas de Infraestructuras Virtuales (IV) y Desarrollo de Aplicaciones para Internet (DAI) de la UGR en 2015-16

##Descripción

Este proyecto consiste en crear la infraestructura para el alojamiento, funcionamiento y despliegue de una aplicación web. Será un proyecto que irá de la mano con el de la asignatura de DAI.

La idea se centra en realizar una aplicación web que funcione como un marco de desarrollo ágil, en el que las personas que trabajen en un proyecto puedan apoyarse para facilitar la organización del equipo de trabajo y el desarrollo de las diferentes partes que conforman el proyecto.

Me voy a basar en [**Scrum**](https://es.wikipedia.org/wiki/Scrum), centrandome por ahora en el **Scrum Taskboard*, que sería así como un tablero con las diferentes tareas a realizar para el desarrollo de un proyecto y que muestra lo que sucede en todo momento en la fase de desarrollo. Las tareas pasan a través de diferentes fases: "Pendiente" en el momento de su creación, "En progreso" cuando alguien está trabajando en ella, ...


##Infraestructura

Al ser una aplicación web necesitaremos que de soporte ofreciendo una infraestructura que cuente con servidores web configurados y adaptados a las necesidades. En este caso lo mejor sería contar con varios servidores junto a un balanceador de carga para mayor rendimiento. Debe desplegar también la base de datos en la que se almacenará la información necesaria para la aplicación.

##Herramientas

- La aplicación web será desarrollada en Python.
- Junto a Python usaremos framework Django
- Para la base de datos SQLite.

Se irán añadiendo más herramientas en la descripción más adelante: utilizar varias herramientas para la replicación de base de datos en el servidor, utilizar RAID para el almacenamiento dentro de los servidores web...


##Integración continua

Para la integración continua de la aplicación he utilizado [Travis](https://travis-ci.org/) que permite soporte para el lenguaje de programación que utilizo y me permite trabajar directamente con este repositorio de github de forma fácil.

###Pasos

Accedemos a la página web de travis (si no estamos dados de alta podemos hacerlo con la cuenta de github). Ya en nuestro perfil nos aparecen directamente los repositorios de Github en los que contribuimos.

Tan solo tenemos que activar nuestro repositorio.

![Repositorio activado a través de Travis](http://i1175.photobucket.com/albums/r628/jesusgorillo/travis_activado_zpsuuttlvkl.png)

Ahora tenemos que definir el archivo de configuración de la integración continua, en este caso es un archivo *.yml*, en el que indicamos el lenguaje, la versión, como instalar dependencias y ejecutar los tests (se pueden añadir más cosas). Para mi caso quedaría tal que así:

```
	language: python
	python:
	 - "3.4"
	before_install:
	 - cd proyecto
	# command to install dependencies
	install:
	 - make install
	# command to run tests
	script:
	 - make test
```

Una vez creado lo subimos al directorio raíz de nuestro repositorio. A continuación accedemos a las propiedades del repositorio y dentro del menú **Webhooks & services** pulsamos sobre Travis CI y seguidamente pulsamos en el botón superior que indica **Test service**.

![Menú del repositorio para activar el test](http://i1175.photobucket.com/albums/r628/jesusgorillo/test_service_zpsexufhaht.png)

Ahora si nos vamos a la web de Travis podremos ver que se están realizando las operaciones pertinentes, y debería completarse con éxito todo el proceso. Recibiriamos un resultado parecido al siguiente:

![Resultado de la operación de integración continua](http://i1175.photobucket.com/albums/r628/jesusgorillo/travis_completado_zpshb1sstys.png)

##Desarrollo basado en pruebas

Para las pruebas para el despliegue de la aplicación he utilizado el sistema de test que ofrece Django, que utiliza un archivo llamado *test.py* en el que escribimos todos los tests que deseemos. Básicamente he utilizado este método porque tiene una estructura muy sencilla y es fácil de utilizar, además no es necesario instalar nada ya que viene incorporado. Puede consultar información [aquí](https://docs.djangoproject.com/en/1.8/topics/testing/).

Los test que he realizado hasta ahora, ya que no tengo avanzado el desarrollo del proyecto, son de los modelos de datos que voy a utilizar para guardar información y de los formularios para insertar información según esos modelos.

El archivo con los tests que he realizado se pueden ver [aquí](https://github.com/JesGor/Proyecto-IV-DAI/blob/master/proyecto/scrumpy/tests.py).

##Comandos básicos

###Setup
	`make install`
###Test
	`make test`
###Run
	`make run`

