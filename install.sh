#!/bin/bash

sudo apt-get update
#Instalar librerias
sudo apt-get install -y python3-setuptools python3-dev build-essential libpq-dev
#Instalar pip
sudo apt-get install -y python3-pip
#Instalar dependencias
sudo pip3 install -r requirements.txt
#SyncDB
sudo python3 manage.py migrate --noinput
