#Despliegue en IaaS - Azure

Para realizar el despliegue en **Azure** necesitamos una serie de paquetes y programas.

* CLI de azure para trabajar con nuestra cuenta desde la línea de comandos.

```
$ apt-get install nodejs-legacy
$ apt-get install npm
$ npm install -g azure-cli
```

* Ansible para el provisionamiento de la máquina virtual.

`$ pip install paramiko PyYAML jinja2 httplib2 ansible`

* Vagrant para la creación de máquinas virtuales y el plugin de Azure.

```
$ apt-get install vagrant
$ vagrant plugin install vagrant-azure
```

Empezamos utilizando el CLI de Azure para conectarnos a nuestra cuenta.

`$ azure login`

Cuando introduzcamos este comando nos proporcionarán un código y un enlace, tenemos que insertar ese código en el enlace para loguearnos después con nuestra cuenta.

![Login de azure a través de CLI](http://i1175.photobucket.com/albums/r628/jesusgorillo/cap1_zpso6ly4tgd.png)

Tenemos ahora que configurar una serie de credenciales.

`$ azure account download`

![Configuración de credenciales](http://i1175.photobucket.com/albums/r628/jesusgorillo/cap2_zpsrnzkrbcc.png)

Aquí otra vez se nos proporciona un enlace, tenemos que acceder a él y obtener mediante descarga las credenciales.

![Obtención de credenciales](http://i1175.photobucket.com/albums/r628/jesusgorillo/cap3_zpsyleo3inm.png)

La credencial descargada tenemos que importarla.

`$ azure account import <credencial>

![Importación de credencial](http://i1175.photobucket.com/albums/r628/jesusgorillo/cap4_zps75zsqdkt.png)

Para conectarnos con Azure necesitamos generar un par de certificados para la comunicación.

```
$ openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout clave_azure.pem -out clave_azure.pem
$ chmod 600 clave_azure.pem
$ openssl x509 -inform pem -in clave_azure.pem -outform der -out clave_azure.cer
```

Como es lógico, Azure debe disponer del certificado creado para la comunicación. Desde el [siguiente enlace](https://manage.windowsazure.com/), en el apartado **Settings** y **MANAGEMENT CERTIFICATES** podemos subir el certificado. Solo es necesario subir el *.cer*.

![Importar certificado en azure](http://i1175.photobucket.com/albums/r628/jesusgorillo/cap5_zpsouhbr8r4.png)

- - - 

A continuación, ya que tenemos configurado lo anterior, tenemos que configurar los archivos para crear la máquina virtual y provisionarla adecuadamente.
 
Para crear la máquina virtual necesitamos el fichero donde irá la configuración de la misma, llamado **Vagrantfile**.

La configuración que definimos es:

* Primer bloque: referente al nombre de la "caja", opciones de red y definirla como *localhost*.
* Segundo bloque: certificado de azure, imagen que se usará como base, nombre de la máquina, usuario y contraseña, localización y configuración de puertos.
* Tercer bloque: nombre de usuario y contraseña para conexión ssh
* Cuarto bloque: opciones de provisionamiento e indicar el archivo para tal cosa.


```
# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.vm.box = 'azure'
  config.vm.network "public_network"
  config.vm.network "private_network",ip: "192.168.33.101"
  config.vm.network "forwarded_port", guest: 80, host: 80
  config.vm.define "localhost" do |l|
    l.vm.hostname = "localhost"
  end

  config.vm.provider :azure do |azure, override|
    azure.mgmt_certificate = File.expand_path('~/IV/clave_azure.pem') 
    azure.mgmt_endpoint = 'https://management.core.windows.net'
    azure.subscription_id = '832dc55f-efb3-472f-b8b7-7472ae52ba58'
    azure.vm_image = 'b39f27a8b8c64d52b05eac6a62ebad85__Ubuntu-14_04_2-LTS-amd64-server-20150506-en-us-30GB'
    azure.vm_name = 'proyecto-iv-dai'
    azure.vm_user = 'bareteca'
    azure.cloud_service_name = 'bareteca'  
    azure.vm_password = 'P4ss.bareteca'
    azure.vm_location = 'Central US' 
    azure.ssh_port = '22'
    azure.tcp_endpoints = '8000:80'
  end   
  
  config.ssh.username = 'bareteca' 
  config.ssh.password = 'P4ss.bareteca'

  
  config.vm.provision "ansible" do |ansible|
    ansible.sudo = true
    ansible.playbook = "provision_azure.yml"
    ansible.verbose = "v"
    ansible.host_key_checking = false
  end

end
```

> La opción *azure.cloud_service_name* va ligada a la dirección DNS que tendrá la aplicación. En este caso será bareteca.cloudapp.net

Necesitamos para el aprovisionamiento de la máquina virtual el archivo *yml*, en este caso lo he llamado **provision_azure.yml** (lo utilizamos en el cuarto bloque del archivo anterior **Vagrantfile**).

En este archivo van los paquetes e instrucciones para preparar la máquina virtual para que ejecute la aplicación. Ponemos como objetivo la máquina *localhost*, e instalamos librerias y paquetes necesarios, se descarga el repositorio y se lanza la aplicación.

```
- hosts: localhost
  sudo: yes
  remote_user: bareteca
  tasks:
  - name: Realizar upgrade
    apt: update_cache=yes
  - name: Instalar librerias python3
    apt: name=python3-setuptools state=present
    apt: name=python3-dev state=present
    apt: name=build-essential state=present
    apt: name=libpq-dev state=present
  - name: Instalar pip
    action: apt pkg=python3-pip
  - name: Instalar git
    apt: name=git state=present
  - name: Descargar repositorio
    git: repo=https://github.com/JesGor/Proyecto-IV-DAI.git dest=~/Proyecto-IV-DAI clone=yes force=yes
  - name: Instalar dependencias
    command: sudo pip3 install -r ~/Proyecto-IV-DAI/requirements.txt
  - name: Dar permisos para ejecución
    command: chmod -R +x ~/Proyecto-IV-DAI
  - name: Instalar/Sincronizar base de datos
    command: sudo python3 ~/Proyecto-IV-DAI/manage.py migrate --noinput
  - name: Ejecutar app
    command: nohup sudo python3 ~/Proyecto-IV-DAI/manage.py runserver 0.0.0.0:8000
```

> se utiliza *nohup* para que la aplicación se quede en ejecución al cerrar la consola.

También necesitamos de un archivo llamado **ansible_hosts** en el que indicaremos el host (máquina virtual) que será objetivo del provisionamiento. Aquí tenemos que indicar la IP que indicamos en el archivo **Vagrantfile**.

```
[localhost]
192.168.33.101
```

Con todos los archivos preparados solo nos queda ejecutar el despliegue.

`$ vagrant up --provider=azure`

El proceso tardará unos minutos, y si todo ha salido correctamente podremos acceder a nuestra aplicación ya desplegada en azure desde la dirección http://bareteca.cloudapp.net

![Aplicación web desplegada en máquina virtual de azure](http://i1175.photobucket.com/albums/r628/jesusgorillo/cap6_zpswghgookh.png)

