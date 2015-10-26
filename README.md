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

##Desarrollo basado en pruebas

Para las pruebas para el despliegue de la aplicación he utilizado el sistema de test que ofrece Django. Puede consultar información [aquí](https://docs.djangoproject.com/en/1.8/topics/testing/)

Tan solo con ejecutar el siguiente comando podemos ejecutar los test:

`pyhon manage.py test`

