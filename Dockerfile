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
