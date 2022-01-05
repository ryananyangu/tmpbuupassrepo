release: python manage.py makemigrations
release: python manage.py makemigrations cordinates
release: python manage.py migrate
web: gunicorn --bind 0.0.0.0:$PORT buupass.wsgi:application --log-file -