#!/bin/sh

python manage.py collectstatic --no-input
python manage.py makemigrations 
python manage.py migrate
gunicorn core.wsgi --bind 0.0.0.0:8000