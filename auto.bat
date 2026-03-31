cd aula
pip install mysqlclient
pip install -r "requirements.txt"
python manage.py makemigrations
python manage.py migrate
python wrapper_pessoas.py
python manage.py runserver