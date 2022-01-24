release: python manage.py makemigrations
release: python manage.py migrate
# release: python manage.py makemigrations accessctrl
# release: python manage.py migrate accessctrl
 
web: gunicorn --bind 0.0.0.0:$PORT buupass.wsgi:application --log-file -