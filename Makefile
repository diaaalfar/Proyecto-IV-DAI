
install:
	sudo apt-get update
	#Instalar librerias
	sudo apt-get install -y python3-setuptools python3-dev build-essential libpq-dev
	#Instalar pip
	sudo apt-get install -y python3-pip
	#Instalar dependencias
	sudo pip3 install -r requirements.txt
	#SyncDB
	sudo python3 manage.py migrate --noinput
	
run:
	python3 manage.py runserver 0.0.0.0:8000

test:
	python3 manage.py test

deploy_heroku:
	chmod +x deploy.sh
	./deploy.sh
	
docker:
	chmod +x docker.sh
	./docker.sh
	
deploy_azure:
	chmod +x azure.sh
	./azure.sh
