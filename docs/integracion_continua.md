#Integración Continua

Necesitamos para la integración continua:

- El fichero [requirements.txt](hhttps://github.com/JesGor/Proyecto-IV-DAI/blob/master/requirements.txt), en el que se indica información de las dependencias (he utilizado el comando `pip freeze`para conocer estas). 

> Esto también puede hacerse con el fichero **setup.py** pero hay que indicar las dependencias en él.

- El fichero de [tests](https://github.com/JesGor/Proyecto-IV-DAI/blob/master/core/tests.py) mencionado en el punto anterior.


##Travis

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

##Snap CI

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

Creamos un stage de tipo **Deploy**  para **heroku**, conectandolo a la cuenta de la misma y seleccionando la aplicación que creamos en la PaaS.

![Creación del stage para desplegar la aplicación en heroku](http://i1175.photobucket.com/albums/r628/jesusgorillo/cap10_zpsvgt6s8lq.png)

Añadimos el último stage referente a la base de datos, que ejecutará un comando para crear la base de datos una vez desplegada la app con los modelos definidos en la aplicación. El comando es `$ heroku run --app scrumpy python manage.py migrate --noinput`.

![Stage con el comando para la creación de la base de datos en heroku](http://i1175.photobucket.com/albums/r628/jesusgorillo/cap14_zpsmhuzqztn.png)

Por último, pulsamos en el botón de ![Botón para crear el proceso de integración continua](http://i1175.photobucket.com/albums/r628/jesusgorillo/cap11_zps3mwkwf2t.png) para crear el proceso de integración continua.

> Si tenemos algún error con la versión de python, cambiarla en el apartado de edición de **Build Pipeline** donde creamos los stages.

La página cambia ahora a mostrarnos el proceso de integración continua y despliegue con los diferentes stages que hemos configurado. Si todo está correctamente nos aparecerá lo siguiente.

![Proceso completado con éxito en Snap CI](http://i1175.photobucket.com/albums/r628/jesusgorillo/cap15_zpswr3r7unr.png)

Hemos pasado todos los stages, y se ha realizado el despliegue en **heroku**. Podemos comprobarlo desde el **Dashboard** del PaaS, accediendo a la aplicación y a la pestaña **Activity**.

![Pestaña Activity con la información de despliegue de la aplicación hecha desde Snap CI](http://i1175.photobucket.com/albums/r628/jesusgorillo/cap13_zpsk5hlca5v.png)

Ahora ya está listo para el proceso de integración continua y el despliegue automático, cuando trabajemos con nuestro repositorio en github se realizará este proceso al realizar un `$ git push`.