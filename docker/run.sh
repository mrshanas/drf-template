#!/bin/sh

set -e

# python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate


# uwsgi --ini ./uwsgi.ini
# uncomment the line below when you want to deploy using wsgi

# uwsgi --socket :9000 --workers 4 --master --enable-threads --module config.wsgi