release: python manage.py makemigrations admin
release: python manage.py makemigrations auth
release: python manage.py makemigrations contenttypes 
release: python manage.py makemigrations sessions
release: python manage.py makemigrations accessctrl
release: python manage.py migrate
release: python manage.py collectstatic




web: gunicorn --bind 0.0.0.0:$PORT buupass.wsgi:application --log-file -