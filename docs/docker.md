#Entorno de pruebas - Docker

Para poder crear una imagen con el entorno necesitamos crear un fichero, llamado **Dockerfile**, en el que indicamos algunas opciones para su configuración, tanto del sistema de la imagen como de la aplicación. En este caso mi Dockerfile es este:

```
FROM ubuntu:14.04
MAINTAINER Jesus Prieto Lopez <jesusgorillo@gmail.com>

#Actualizar los repositorios
RUN sudo apt-get -y update

#Instalar la herramienta GIT
RUN sudo apt-get install -y git

#Descargamos el proyecto
RUN sudo git clone https://github.com/JesGor/Proyecto-IV-DAI.git

#Instalamos python3
RUN sudo apt-get install -y python3-setuptools python3-dev build-essential libpq-dev
RUN sudo easy_install3 pip
RUN sudo pip install --upgrade pip

#Instalar las dependencias
RUN cd Proyecto-IV-DAI && pip install -r requirements.txt

#Sincronización de la base de datos
RUN cd Proyecto-IV-DAI && python3 manage.py migrate --noinput
```

Como queremos que se construya automáticamente la imagen con la aplicación hacemos uso de la página web de [Docker Hub](https://hub.docker.com/). Tenemos que registarnos y asociar la cuenta con la de *GitHub*.

![Imagen de cuenta asociada con github](http://i1175.photobucket.com/albums/r628/jesusgorillo/cap1_zpsqovcohyp.png)

Hecho esto, desde el botón ![Botón de crear en docker hub](http://i1175.photobucket.com/albums/r628/jesusgorillo/cap2_zpsef99rhzi.png) seleccionamos la opción **Create Automated Build**. Seleccionamos el repositorio donde está nuestra aplicación y después pulsamos en el botón **Create** que nos aparecerá. Tarda unos minutos en crear la build.

Mi imagen puede encontrarse [aquí](https://hub.docker.com/r/jesgor/proyecto-iv-dai/).

![Imagen del repositorio creado en docker hub](http://i1175.photobucket.com/albums/r628/jesusgorillo/cap3_zpsfk6uho6v.png)

Terminado el proceso ya podemos disponer de la imagen para trabajar con ella en nuestro ordenador. Esta imagen se actualizará según realizamos modificaciones en el repositorio de la aplicación.

Para descargar la imagen:

`$ docker pull jesgor/proyecto-iv-dai`

Para ejecutarla:

`$ sudo docker run -i -t jesgor/proyecto-iv-dai /bin/bash`

He automátizado estos dos pasos mediante un script, llamado *docker.sh*.

```
#!/bin/bash

#Descarga docker
sudo wget -qO- https://get.docker.com/ | sh
# Inicia el servicio docker
sudo service docker start
#Descarga la imagen
sudo docker pull jesgor/proyecto-iv-dai
#Ejecuta la imagen
sudo docker run -i -t jesgor/proyecto-iv-dai /bin/bash 
```

Ya dentro del contenedor podemos ejecutar la aplicación del proyecto como si estuviésemos en el sistema anfitrión.

`$ cd Proyecto-IV-DAI`
`$ python3 manage.py runserver`

Obtenemos la ip del contenedor con el comando `$ ifconfig` y desde un navegador del sistema anfitrión introducir la ip correspondiente para visualizar la aplicación (mientras está este arrancada).

![Página principal del proyecto ejecutado desde el contenedor](http://i1175.photobucket.com/albums/r628/jesusgorillo/cap29_zpsdqzqw3bq.png)

> Si desde el navegador del sistema anfitrión no se pudiera acceder a la aplicación web, ejecute el comando `$ python3 manage.py runserver,`anteriormente mencionado, seguido de `0.0.0.0:8000`. 