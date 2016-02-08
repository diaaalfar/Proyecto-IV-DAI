#!/bin/bash

#Instalar vagrant
sudo apt-get install -y vagrant
#Instalar plugin azure
sudo vagrant plugin install vagrant-azure
#Instalar pip
sudo apt-get install -y python-pip
#Instalar ansible
sudo pip install paramiko PyYAML jinja2 httplib2 ansible
#Instalar fabric
sudo apt-get install -y fabric
#Creación y provisionamiento de máquina virtual mediante archivo Vagrantfile y .yml
sudo vagrant up --provider=azure
#Despliegue/Inicio de la aplicación a través de fabric
sudo fab -H bareteca@bareteca.cloudapp.net run_app
