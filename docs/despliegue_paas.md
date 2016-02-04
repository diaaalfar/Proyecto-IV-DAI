#Despliegue en PaaS - heroku

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
$ heroku apps:rename bareteca
```

Se nos proporciona el add-ons de **heroku** para base de datos postgresql. En esta aplicacion usaremos sqlite en local, pero a la hora de desplegarlo en el PaaS usaremos postgresql. Tenemos que configurar la aplicacicón. 

Si accedemos al add-on de Postgres que disponemos en la pestaña **Resources**  en la aplicación de **heroku** se nos muestra información de la base de datos que usaremos.

![Icono del add-on para la base de datos postgresql](http://i1175.photobucket.com/albums/r628/jesusgorillo/cap17_zpsxd0bimvl.png)

![Información de la base de datos](http://i1175.photobucket.com/albums/r628/jesusgorillo/cap4_zpsv10vew1v.png)

Nos quedamos con el apartado de URL, para conectar a la base de datos desde la aplicación. En el archivo *settings.py*, que está en el directorio *bareteca* tenemos que añadir el código para indicar que, si está la aplicación en heroku, utilice la base de datos con la información necesaria.

```python
DEPLOY_HEROKU = os.environ.get('PORT')
if DEPLOY_HEROKU:
    DATABASE_URL='postgres://ohgvaeuqofzbdr:J0NJELBfg3d3UAOikpu9PwWYpS@ec2-54-204-30-115.compute-1.amazonaws.com:5432/do847mn2mbgdu'
    DATABASES = {'default': dj_database_url.config(default=DATABASE_URL)}
```

Podemos conectar la aplicacion desde el PaaS al repositorio donde subimos nuestro codigo que vamos desarrollando. Desde la web de **heroku**, en nuestro **Dashboard** accedemos a nuestra aplicación y en la pestaña **Deploy** conectamos la aplicación con **github**.

![Pestaña Deploy en las opciones de la aplicacion en heroku](http://i1175.photobucket.com/albums/r628/jesusgorillo/cap7_zpsupcphlqp.png)

Indicamos el repositorio con el que queremos conectar en el apartado **Connect to Github**.

![Repositorio que conectar con la aplicación](http://i1175.photobucket.com/albums/r628/jesusgorillo/cap5_zpsysj7kwam.png)

También he activado la opción de realizar el despliegue automático desde la rama *master*, y que espere a la integración continua antes de desplegarse (ya que la configuro con Snap-CI).

![Activar despliegue automático después de CI](http://i1175.photobucket.com/albums/r628/jesusgorillo/cap16_zpslfn0szm2.png)

Subimos los fuentes de la aplicacicón y los archivos creados anteriormente a **heroku** con `$ git add`, `$ git commit` y `$ git push heroku master`.

![Añadiendo los fuentes al PaaS heroku](http://i1175.photobucket.com/albums/r628/jesusgorillo/cap2_zpszgpncrvc.png)

Y ejecutamos el comando necesario para que se configure la base de datos.

`$ heroku run python manage.py migrate`

Para finalizar accedemos a [esta dirección](https://proyecto-iv-dai.herokuapp.com/) para ver la aplicación desplegada o usamos el comando `$ heroku open` desde local.