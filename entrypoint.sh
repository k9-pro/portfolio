#!/bin/sh

#pip install gunicorn
#pip install -r requirements.txt

#python3 migrate.py migrate
mkdir /srv/docker-server/static
python3 manage.py collectstatic


gunicorn config.wsgi:application --bind 0.0.0.0:8888

