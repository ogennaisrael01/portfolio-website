#!/usr/bin/env bash
set -o errexit

python manage.py migrate --noinput
python manage.py create_user || true
python manage.py seed || true

gunicorn portfolio_site.wsgi:application --bind 0.0.0.0:$PORT
