#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

echo "Makemigrations..."
python manage.py makemigrations
echo "Migrate..."
python manage.py createsuperuser --noinput --username=$DJANGO_SUPERUSER_ADMIN --email=$DJANGO_SUPERUSER_EMAIL 
echo "Create superuser..."
python manage.py migrate
echo "Collectstatic..."
python manage.py collectstatic --no-input

exec "$@"