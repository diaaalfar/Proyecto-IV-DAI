#!/bin/bash

#Descarga docker
sudo wget -qO- https://get.docker.com/ | sh
# Inicia el servicio docker
sudo service docker start
#Descarga la imagen
sudo docker pull jesgor/proyecto-iv-dai
#Ejecuta la imagen
sudo docker run -i -t jesgor/proyecto-iv-dai /bin/bash 
