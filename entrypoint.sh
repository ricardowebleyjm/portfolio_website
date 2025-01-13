#!/bin/bash

echo "Collecting static files"
python manage.py collectstatic --noinput

echo "Starting Gunicorn"
gunicorn portfolio_website.wsgi:application --bind 0.0.0.0:8000