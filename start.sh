pipenv --python 3.12

pipenv run python manage.py collectstatic --noinput
pipenv run python manage.py makemigrations --noinput
pipenv run python manage.py migrate --noinput

pipenv run python manage.py shell -c "from webchat.models import Usuario; \
    Usuario.objects.filter(username='zeca').exists() or \
    Usuario.objects.create_superuser('zeca',
    'zeca@example.com', 'senha123'); \
    Usuario.objects.filter(username='cuca').exists() or \
    Usuario.objects.create_superuser('cuca',
    'cuca@example.com', 'senha123')"
./runDocker
