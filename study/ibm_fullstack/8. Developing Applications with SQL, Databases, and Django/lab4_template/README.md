This project need the below commands executed to be successfully run
inside root folder lab4_template create a virtual env

- pipenv shell

it will install all the modules in the requirements.txt file automatically
it didn't install wheel module automatically so run the below to install that module

- pipenv install wheel==0.37.1

install postgres python connector module

- pipenv install psycopg2-binary

in the settings.py file inside myproject folder give the username password for the postgres db
here i'm using a python module called passwords created by me for getting the password and username
Create tables and migrate using below commands

- pipenv run python manage.py makemigrations
- pipenv run python manage.py migrate

Creating a super user for the admin panel can be done by below command

- run python manage.py createsuperuser

To run the server use the below command

- pipenv run python manage.py runserver

Once register models defined in adminsite/models.py with admin site, those models need to be added in adminsite/admin.py to active in the admin panel

- admin.site.register(Course)
- admin.site.register(Instructor)

We can assign any user to be an instructor by clicking the add button next to instructor and selecting a user from there

If need to include only some of the model fields in the admin site.
create a class in adminsite/admin.py file and add needed fields then edit the register with the custom one

- class CustomCourseAdmin(admin.ModelAdmin):

  - fields = ['pub_date', 'name', 'description']

- admin.site.register(Course, CustomCourseAdmin)
