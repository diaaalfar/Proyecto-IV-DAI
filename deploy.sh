#!/bin/bash

heroku login
heroku create
git add .
git commit -m "Desplegando aplicación en heroku"
git push heroku master
heroku run python manage.py migrate --noinput
heroku ps:scale web=1
