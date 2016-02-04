# Proyecto-IV-DAI
# *Bareteca*
Jesús Prieto López

[![Build Status](https://travis-ci.org/JesGor/Proyecto-IV-DAI.svg?branch=master)](https://travis-ci.org/JesGor/Proyecto-IV-DAI)
[![Build Status](https://snap-ci.com/JesGor/Proyecto-IV-DAI/branch/master/build_image)](https://snap-ci.com/JesGor/Proyecto-IV-DAI/branch/master)
[![Heroku](https://www.herokucdn.com/deploy/button.png)](https://http://proyecto-iv-dai.herokuapp.com/.herokuapp.com/)

Repositorio dedicado al proyecto de las asignaturas de Infraestructuras Virtuales (IV) y Desarrollo de Aplicaciones para Internet (DAI) de la UGR en 2015-16.

##Índice

1. [Descripción](#descripción)
2. [Infraestructura](#infraestructura)
3. [Herramientas](herramientas)
4. [Herramienta de construcción](#herramienta-de-construcción)
5. [Desarrollo basado en prubas](#desarrollo-basado-en-pruebas)
6. [Despliegue en PaaS - Heroku](#despliegue-en-paas---heroku)
7. [Integración Continua](#integración-continua)
8. [Entorno de prubas - Docker](#entorno-de-pruebas---docker)
9. [Comando básicos](#comandos-básicos)

##Descripción

Este proyecto consiste en crear la infraestructura para el alojamiento, funcionamiento y despliegue de una aplicación web. Será un proyecto que irá de la mano con el de la asignatura de DAI.

La idea se centra en realizar una aplicación web que funcione como un portal de información acerca de bares que visitar, donde se pueden localizar estos y tapas que hay disponibles.

El portal cuenta con un listado de bares junto a una gráfica con los bares más visitados. Dentro de cada bar tenemos información de este, como la localización por medio de un plugin que muestra el mapa y un listado de sus tapas. Cada tapa tiene un nº de votos que podemos ir aumentando al votarlas.

Esta web permite realizar el registro de usuario y la identificación de los mismos, que podrán añadir tapas a la base de datos.


##Infraestructura

Al ser una aplicación web necesitaremos que de soporte ofreciendo una infraestructura que cuente con un servidor web para desplegar la aplicación y que se ejecute en él. Debe desplegar también la base de datos en la que se almacenará la información necesaria para la aplicación.

La infraestructura que utilizo en este proyecto es la que me proporciona una plataforma PaaS como es **heroku**. También hago uso de contenedores con **docker**. Y por último también utilizo máquinas virtuales que me proporciona **Azure**.

##Herramientas

- La aplicación web será desarrollada en Python.
- Junto a Python usaremos framework Django
- Para la base de datos SQLite. En Heroku utilizamos PostgreSQL
- [heroku](heroku.com) como PaaS para desplegar la aplicación
- [Docker](www.docker.com) para crear contenedores
- [Azure](azure.microsoft.com/es-es/) como IaaS para crear máquinas virtuales
- [Snap-CI](snap-ci.com) y [Travis](travis-ci.org) para integración continua
- [django-registration-redux](django-registration-redux.readthedocs.org/en/latest/) para el registro y login de usuarios
- [django-easy-maps](github.com/bashu/django-easy-maps) para los mapas de los bares
- [Bootstrap](getbootstrap.com) para el estilo de la aplicación##Herramienta de construcción

Como herramienta de construcción he utilizado el archivo que por defecto crea el proyecto de Django, **manage.py**, el cual permite realizar varias operaciones de control, como ejecutar la aplicación o los test. Para la instalación de dependencias se hace uso de **requirements.txt** que podemos crear con `$ pip freeze` o el archivo **setup.py**.

- Ejecutar la aplicación `$ python manage.py runserver`
- Realizar los test `$ python manage.py test`
- Instalar dependencias `$ pip install -r requirements.txt`

Por ejemplo, podemos probar a ejecutar el comando para iniciar la aplicación y ver los resultados

`$ python manage.py runserver`


##Desarrollo basado en pruebas

Para las pruebas para el despliegue de la aplicación he utilizado el sistema de test que ofrece Django, que utiliza un archivo llamado *test.py* en el que escribimos todos los tests que deseemos. Básicamente he utilizado este método porque tiene una estructura muy sencilla y es fácil de utilizar, además no es necesario instalar nada ya que viene incorporado. Puede consultar información [aquí](https://docs.djangoproject.com/en/1.8/topics/testing/).

Los test que he realizado hasta ahora, ya que no tengo avanzado el desarrollo del proyecto, son de los modelos de datos que voy a utilizar para guardar información y de los formularios para insertar información según esos modelos.

El archivo con los tests que he realizado se pueden ver [aquí](https://github.com/JesGor/Proyecto-IV-DAI/blob/master/core/tests.py).

Prueba los tests con el siguiente comando:

`$ python manage.py test`


##Despliegue en Paas - Heroku

Para el despligue de la aplicación he utilizado el Paas [heroku](https://www.heroku.com/) que me permite trabajar con el repositorio github directamente conectándolo a él, y realizar conjunta la integración continua con **Snap CI** antes de desplegarlo. He elegido **heroku** como PaaS porque he trabajado en la asignatura IV con este y la verdad que es muy fácil de usar.

Podemos encontrar en [este enlace](https://proyecto-iv-dai.herokuapp.com/) la aplicación desplegada.

> Una vez completada la configuración de despliegue en **heroku** y comprobado que funcionaba, he automatizado el proceso de despliegue junto al proceso de integración continua con **Snap CI**. Esto se explica en el apartado de [Integración continua - Snap CI](https://github.com/JesGor/Proyecto-IV-DAI/blob/master/docs/integracion_continua.md#snap-ci)

Se ha automatizado el despliegue en heroku con el script [deploy.sh](https://github.com/JesGor/Proyecto-IV-DAI/blob/master/deploy.sh).

Para ver el proceso pulse en el siguiente enlace:
>####[Más informacion](https://github.com/JesGor/Proyecto-IV-DAI/blob/master/docs/despliegue_paas.md)

##Integración continua

Para la integración continua de la aplicación he utilizado [Travis](https://travis-ci.org/) que permite soporte para el lenguaje de programación que utilizo y me permite trabajar directamente con este repositorio de github de forma fácil. 

También he utlizado [Snap CI](https://snap-ci.com/) para que realice la integración continua junto al despliegue en **heroku**.

Para ver el proceso pulse en el siguiente enlace:
>####[Más informacion](https://github.com/JesGor/Proyecto-IV-DAI/blob/master/docs/integracion_continua.md)


##Entorno de pruebas - Docker

En lo que a entorno de pruebas se refiere he utilizado la herramienta **Docker**, que permite trabajar con contenedores para disponer así de un entorno aislado para la aplicación. Desde este entorno podemos probar la aplicación o desplegarla.

La imagen está situada en la página de [Docker Hub](https://hub.docker.com), concretamente [aquí](https://hub.docker.com/r/jesgor/proyecto-iv-dai/).

Para disponer del entorno de pruebas e iniciarlo, ejecuta el archivo [docker.sh](https://github.com/JesGor/Proyecto-IV-DAI/blob/master/docker.sh).

Para ver el proceso pulse en el siguiente enlace:
>####[Más informacion](https://github.com/JesGor/Proyecto-IV-DAI/blob/master/docs/docker.md)


##Comandos básicos

###Instalar python3
	$ apt-get install -y python3-setuptools python3-dev build-essential libpq-dev
### Instalar pip
	$ sudo easy_install3 pip
###Instalar dependencias
	$ pip install -r requirements.txt
###Sincronizar base de datos
	$ python manage.py migrate --noinput
###Test
	$ python manage.py test
###Arrancar aplicación
	$ python manage.py runserver
###Despliegue en heroku
	$ ./deploy.sh
###Instalar imagen de entorno docker
	$ ./docker.sh