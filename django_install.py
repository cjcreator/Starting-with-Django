GNU nano 6.3         django_install.py
pip install virtualenv

pwd
mkdir django
cd django
ls
#creating virtual envirnment
virtualenv trydjango

cd trydjango
pip install Django
ls
source bin/activate
mkdir src #create a directory src
ls
cd src
python -m django-admin startproject trydjango
#starting project
cd trydjango
ls
python manage.py runserver
#copy the link and paste in browser
