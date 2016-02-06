#!/bin/bash

#Instalar vagrant
sudo apt-get install -y vagrant
#Instalar plugin azure
sudo vagrant plugin install vagrant-azure
#Instalar pip
sudo apt-get install -y python-pip
#Instalar ansible
sudo pip install paramiko PyYAML jinja2 httplib2 ansible
#Desplegar con vagrant y provisionar con ansible en azure
sudo vagrant up --provider=azure
