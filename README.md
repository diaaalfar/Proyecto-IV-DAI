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

##Herramienta de construcción

Como herramienta de construcción he utilizado el archivo que por defecto crea el proyecto de Django, **manage.py**, el cual permite realizar varias operaciones de control, como ejecutar la aplicación o los test. Para la instalación de dependencias se hace uso de **requirements.txt** que podemos crear con `$ pip freeze` o el archivo **setup.py**.

- Ejecutar la aplicación `$ python manage.py runserver`
- Realizar los test `$ python manage.py test`
- Instalar dependencias `$ pip install -r requirements.txt`

Por ejemplo, podemos probar a ejecutar el comando para iniciar la aplicación y ver los resultados

`$ python manage.py runserver`

![Resultado del comando run](http://i1175.photobucket.com/albums/r628/jesusgorillo/make_run_zpsyztzax0u.png)

##Desarrollo basado en pruebas

Para las pruebas para el despliegue de la aplicación he utilizado el sistema de test que ofrece Django, que utiliza un archivo llamado *test.py* en el que escribimos todos los tests que deseemos. Básicamente he utilizado este método porque tiene una estructura muy sencilla y es fácil de utilizar, además no es necesario instalar nada ya que viene incorporado. Puede consultar información [aquí](https://docs.djangoproject.com/en/1.8/topics/testing/).

Los test que he realizado hasta ahora, ya que no tengo avanzado el desarrollo del proyecto, son de los modelos de datos que voy a utilizar para guardar información y de los formularios para insertar información según esos modelos.

El archivo con los tests que he realizado se pueden ver [aquí](https://github.com/JesGor/Proyecto-IV-DAI/blob/master/scrumpy/tests.py).

Prueba los tests con el siguiente comando:

`$ python manage.py test`

![Resultado del comando make test](http://i1175.photobucket.com/albums/r628/jesusgorillo/make_test_zps4jeexsb8.png)


##Integración continua

Para la integración continua de la aplicación he utilizado [Travis](https://travis-ci.org/) que permite soporte para el lenguaje de programación que utilizo y me permite trabajar directamente con este repositorio de github de forma fácil. 

También he utlizado [Snap CI](https://snap-ci.com/) para que realice la integración continua junto al despliegue en **Heroku**.

Necesitamos para la integración continua:

- El fichero [requirements.txt](hhttps://github.com/JesGor/Proyecto-IV-DAI/blob/master/requirements.txt), en el que se indica información de las dependencias (he utilizado el comando `pip freeze`para conocer estas). 

> Esto también puede hacerse con el fichero **setup.py** pero hay que indicar las dependencias en él.

- El fichero de [tests](https://github.com/JesGor/Proyecto-IV-DAI/blob/master/scrumpy/tests.py) mencionado en el punto anterior.


###Travis

Accedemos a la página web de travis (si no estamos dados de alta podemos hacerlo con la cuenta de github). Ya en nuestro perfil nos aparecen directamente los repositorios de Github en los que contribuimos.

Tan solo tenemos que activar nuestro repositorio.

![Repositorio activado a través de Travis](http://i1175.photobucket.com/albums/r628/jesusgorillo/travis_activado_zpsuuttlvkl.png)

Ahora tenemos que definir el archivo de configuración de la integración continua, en este caso es un archivo *.yml*, en el que indicamos el lenguaje, la versión, como instalar dependencias y ejecutar los tests (se pueden añadir más cosas). Para mi caso quedaría tal que así:

```
language: python
python:
 - "3.4"
# command to install dependencies
install:
 - pip install -r requirements.txt
# command to run tests
script:
 - python manage.py test
```

Una vez creado lo subimos al directorio raíz de nuestro repositorio. A continuación accedemos a las propiedades del repositorio y dentro del menú **Webhooks & services** pulsamos sobre Travis CI y seguidamente pulsamos en el botón superior que indica **Test service**.

![Menú del repositorio para activar el test](http://i1175.photobucket.com/albums/r628/jesusgorillo/test_service_zpsexufhaht.png)

Ahora si nos vamos a la web de Travis podremos ver que se están realizando las operaciones pertinentes, y debería completarse con éxito todo el proceso. Recibiríamos un resultado parecido al siguiente:

![Resultado de la operación de integración continua](http://i1175.photobucket.com/albums/r628/jesusgorillo/travis_completado_zpshb1sstys.png)

###Snap CI

##Despliegue en Paas - Heroku

Para el despligue de la aplicación he utilizado el Paas [heroku](https://www.heroku.com/) que me permite trabajar con el repositorio github directamente conectándolo a él, y realizar conjunta la integración continua con **Snap CI** antes de desplegarlo. He elegido **heroku** como PaaS porque he trabajado en la asignatura IV con este y la verdad que es muy fácil de usar.

Para el despliegue en **heroku** necesitamos dos archivos:

- Procfile: Utilizado para que la plataforma ejecute la aplicación, en este caso web.

```
web: gunicorn proyecto.wsgi --log-file -
```

- runtime.txt: Se utiliza para indicar la versión de python

```
python-3.4.0
```

Aparte hay que añadir algunas dependencias al archivo *requirements.txt*, como puede ser *gunicorn* que lo utiliza la plataforma para ejecutar la app y el cinturón de herramientas de django *django-toolbelt*. Puedes consultar el contenido en el enlace [requirements.txt](hhttps://github.com/JesGor/Proyecto-IV-DAI/blob/master/requirements.txt)




##Comandos básicos

###Setup
	$ pip install -r requirements.txt
###Test
	$ python manage.py test
###Run
	$ python manage.py runserver
