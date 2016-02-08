from fabric.api import run
from fabric.contrib import django

def install():
	run('sudo ~/Proyecto-IV-DAI/install.sh')

def run_app():
	run('nohup sudo python3 ~/Proyecto-IV-DAI/manage.py runserver 0.0.0.0:8000')
	
def pull():
	run('cd ~/Proyecto-IV-DAI && sudo git pull')
