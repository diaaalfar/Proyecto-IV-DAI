# Proyecto-IV-DAI
# *Scrumpy*
Jesús Prieto López

[![Build Status](https://travis-ci.org/JesGor/Proyecto-IV-DAI.svg?branch=master)](https://travis-ci.org/JesGor/Proyecto-IV-DAI)
[![Build Status](https://snap-ci.com/JesGor/Proyecto-IV-DAI/branch/master/build_image)](https://snap-ci.com/JesGor/Proyecto-IV-DAI/branch/master)
[![Heroku](https://www.herokucdn.com/deploy/button.png)](https://scrumpy.herokuapp.com/)

Repositorio dedicado al proyecto de las asignaturas de Infraestructuras Virtuales (IV) y Desarrollo de Aplicaciones para Internet (DAI) de la UGR en 2015-16

##Descripción

Este proyecto consiste en crear la infraestructura para el alojamiento, funcionamiento y despliegue de una aplicación web. Será un proyecto que irá de la mano con el de la asignatura de DAI.

La idea se centra en realizar una aplicación web que funcione como un marco de desarrollo ágil, en el que las personas que trabajen en un proyecto puedan apoyarse para facilitar la organización del equipo de trabajo y el desarrollo de las diferentes partes que conforman el proyecto.

Me voy a basar en [**Scrum**](https://es.wikipedia.org/wiki/Scrum), centrandome por ahora en el **Scrum Taskboard**, que sería así como un tablero con las diferentes tareas a realizar para el desarrollo de un proyecto y que muestra lo que sucede en todo momento en la fase de desarrollo. Las tareas pasan a través de diferentes fases: "Pendiente" en el momento de su creación, "En progreso" cuando alguien está trabajando en ella, ...


##Infraestructura

Al ser una aplicación web necesitaremos que de soporte ofreciendo una infraestructura que cuente con servidores web configurados y adaptados a las necesidades. En este caso lo mejor sería contar con varios servidores junto a un balanceador de carga para mayor rendimiento. Debe desplegar también la base de datos en la que se almacenará la información necesaria para la aplicación.

La infraestructura que utilizo en este proyecto es la que me proporciona una plataforma PaaS como es **heroku**.

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


##Desarrollo basado en pruebas

Para las pruebas para el despliegue de la aplicación he utilizado el sistema de test que ofrece Django, que utiliza un archivo llamado *test.py* en el que escribimos todos los tests que deseemos. Básicamente he utilizado este método porque tiene una estructura muy sencilla y es fácil de utilizar, además no es necesario instalar nada ya que viene incorporado. Puede consultar información [aquí](https://docs.djangoproject.com/en/1.8/topics/testing/).

Los test que he realizado hasta ahora, ya que no tengo avanzado el desarrollo del proyecto, son de los modelos de datos que voy a utilizar para guardar información y de los formularios para insertar información según esos modelos.

El archivo con los tests que he realizado se pueden ver [aquí](https://github.com/JesGor/Proyecto-IV-DAI/blob/master/scrumpy/tests.py).

Prueba los tests con el siguiente comando:

`$ python manage.py test`


##Despliegue en Paas - Heroku

Para el despligue de la aplicación he utilizado el Paas [heroku](https://www.heroku.com/) que me permite trabajar con el repositorio github directamente conectándolo a él, y realizar conjunta la integración continua con **Snap CI** antes de desplegarlo. He elegido **heroku** como PaaS porque he trabajado en la asignatura IV con este y la verdad que es muy fácil de usar.

> Una vez completada la configuración de despliegue en **heroku** y comprobado que funcionaba, he automatizado el proceso de despliegue junto al proceso de integración continua con **Snap CI**. Esto se explica en el apartado de [Integración continua - Snap CI](#snap-ci)

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

Es necesario bajarse las herramientas de **heroku** para desplegar la aplicación.

`$ wget -O- https://toolbelt.heroku.com/install-ubuntu.sh | sh `

Una vez instalado nos logueamos con nuestra cuenta mediante el comando:

`$ heroku login`

Accedemos ahora al directorio de nuestra aplicación y creamos nuestra aplicación en **heroku**, la renombramos (pone un nombre aleatorio), y subimos el código fuente.

```
$ heroku create
$ heroku apps:rename scrumpy
```

![Resultado de crear la app y cambiarla de nombre en heroku](http://i1175.photobucket.com/albums/r628/jesusgorillo/cap1_zpsenb3zdcf.png)

Desde la web de **heroku**, en nuestro **Dashboard** accedemos a nuestra aplicación y en la pestaña **Deploy** conectamos la aplicación con **github**.

![Pestaña Deploy en las opciones de la aplicacion en heroku](http://i1175.photobucket.com/albums/r628/jesusgorillo/cap4_zpsswgzfhhw.png)

Indicamos el repositorio con el que queremos conectar en el apartado **Connect to Github**.

![Repositorio que conectar con la aplicación](http://i1175.photobucket.com/albums/r628/jesusgorillo/cap5_zpsysj7kwam.png)

Subimos los fuentes de la aplicacicón y los archivos creados anteriormente a **heroku** con `$ git add`, `$ git commit` y `$ git push heroku master`.

![Añadiendo los fuentes al PaaS heroku](http://i1175.photobucket.com/albums/r628/jesusgorillo/cap2_zpszgpncrvc.png)

![Desplegado de la app en heroku](http://i1175.photobucket.com/albums/r628/jesusgorillo/cap3_zpsbpc23oll.png)

Para finalizar accedemos a [esta dirección](https://scrumpy.herokuapp.com/) para ver la aplicación desplegada o usamos el comando `$ heroku open` desde local.


##Integración continua

Para la integración continua de la aplicación he utilizado [Travis](https://travis-ci.org/) que permite soporte para el lenguaje de programación que utilizo y me permite trabajar directamente con este repositorio de github de forma fácil. 

También he utlizado [Snap CI](https://snap-ci.com/) para que realice la integración continua junto al despliegue en **heroku**.

Necesitamos para la integración continua:

- El fichero [requirements.txt](hhttps://github.com/JesGor/Proyecto-IV-DAI/blob/master/requirements.txt), en el que se indica información de las dependencias (he utilizado el comando `pip freeze`para conocer estas). 

> Esto también puede hacerse con el fichero **setup.py** pero hay que indicar las dependencias en él.

- El fichero de [tests](https://github.com/JesGor/Proyecto-IV-DAI/blob/master/scrumpy/tests.py) mencionado en el punto anterior.


###Travis

Accedemos a la página web de **Travis** (si no estamos dados de alta podemos hacerlo con la cuenta de github). Ya en nuestro perfil nos aparecen directamente los repositorios de Github en los que contribuimos.

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

He utilizado este sistema [Snap CI](https://snap-ci.com/) de integración continua, aparte de **Travis**, porque me permite realizar el proceso de integración junto al proceso de despliegue de la aplicación en el PaaS que he elegido, **heroku**.

Nos registramos en la página web y una vez nos logueamos pedirá permiso para conectarse a nuestra cuenta de Github. Cuando se haga la conexión correctamente se nos mostrará un menú donde elegir el repositorio que queremos conectar para la integración. En caso de estar registrado hay que acceder al menú y añadir repositorio con el botón **+Repository**.

![Menú superior de snap ci](http://i1175.photobucket.com/albums/r628/jesusgorillo/cap6_zpscvtfvc6b.png)

Elegimos el repositorio donde está nuestra aplicación en github.

![Selección del repositorio de github para conectarlo a Snap CI](http://i1175.photobucket.com/albums/r628/jesusgorillo/cap7_zpsbxj6hs3g.png)

Tan pronto añadimos el repositorio, aparece la configuración de los pasos y operaciones, contenidos en **Stages** que se realizan para la integración continua y el despliegue. Por defecto trae solo un paso de instalar dependencias. Hay que editarlo.

Creamos un stage que será para instalar las dependencias, lo llamamos por ejemplo **Install* e indicamos en él el comando para ello `$ pip install -r requirements.txt`, como viene en la siguiente captura.

![Creación del stage de instalación de dependencias para la integración](http://i1175.photobucket.com/albums/r628/jesusgorillo/cap8_zpswgzp6quz.png)

Otro stage para la realización de los tests de la aplicación en si, con la orden `$ python manage.py test`.

![Creación del stage para realizar los test de la aplicación](http://i1175.photobucket.com/albums/r628/jesusgorillo/cap9_zpsrapprrwc.png)

Para el último paso, el de despliegue, creamos un stage de tipo **Deploy**  para **heroku**, conectandolo a la cuenta de la misma y seleccionando la aplicación que creamos en la PaaS.

![Creación del stage para desplegar la aplicación en heroku](http://i1175.photobucket.com/albums/r628/jesusgorillo/cap10_zpsvgt6s8lq.png)

Por último, pulsamos en el botón de ![Botón para crear el proceso de integración continua](http://i1175.photobucket.com/albums/r628/jesusgorillo/cap11_zps3mwkwf2t.png) para crear el proceso de integración continua.

> Si tenemos algún error con la versión de python, cambiarla en el apartado de edición de **Build Pipeline** donde creamos los stages.

La página cambia ahora a mostrarnos el proceso de integración continua y despliegue con los diferentes stages que hemos configurado. Si todo está correctamente nos aparecerá lo siguiente.

![Proceso completado con éxito en Snap CI](http://i1175.photobucket.com/albums/r628/jesusgorillo/cap12_zpsdde8blqr.png)

Hemos pasado todos los stages, y se ha realizado el despliegue en **heroku**. Podemos comprobarlo desde el **Dashboard** del PaaS, accediendo a la aplicación y a la pestaña **Activity**.

![Pestaña Activity con la información de despliegue de la aplicación hecha desde Snap CI](http://i1175.photobucket.com/albums/r628/jesusgorillo/cap13_zpsk5hlca5v.png)

Ahora ya está listo para el proceso de integración continua y el despliegue automático, cuando trabajemos con nuestro repositorio en github se realizará este proceso al realizar un `$ git push`.


##Comandos básicos

###Setup
	$ pip install -r requirements.txt
###Test
	$ python manage.py test
###Run
	$ python manage.py runserver
