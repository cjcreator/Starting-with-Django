
pip install virtualenv
#firstly install the virtual environment
pwd
#create a new directory by using command - mkdir <filename>

mkdir django
cd django #openit
#ls ---listing for linux users
#Dir --listing for windows users

#creating virtual envirnment
virtualenv trydjango

cd trydjango
pip install Django 
#ls ---listing for linux users
#Dir --listing for windows users
#methods to activate virtual environment:
source bin/activate 
#activate👆👆 the virtual environment by using command for linux user
#note:-if you are windows users then type 👇👇
./Scripts/activate.bat
#   Or
cd scripts
Activate.bat



mkdir src #create a directory src
ls
cd src
python -m django-admin startproject trydjango
#starting project
cd trydjango
ls
python manage.py runserver
#copy the link and paste in browser
