pipenv --python 3.12

pipenv run python manage.py collectstatic --noinput
pipenv run python manage.py makemigrations --noinput
pipenv run python manage.py migrate --noinput

pipenv run python manage.py shell -c "from django.contrib.auth.models import User; \
                           User.objects.filter(username='zeca').exists() or \
                           User.objects.create_superuser('zeca',
                           'zeca@example.com', 'senha123'); \
                           User.objects.filter(username='cuca').exists() or \
                           User.objects.create_superuser('cuca',
                           'cuca@example.com', 'senha123')"
./run
