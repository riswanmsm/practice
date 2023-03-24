Create a folder
Navigate into the folder and run pipenv shell to make virtual environment
install Django using pipenv / pipenv install Django
create a new djnago project by running the command / django-admin startproject project_name
go inside the created project folder project_name and run the below command to create an app for the project
./manage.py startapp firstapp
install package to use env file to store db password
pipenv install python-dotenv
install package to connect postgres db
pipenv install psycopg2-binary
./manage.py makemigrations
./manage.py migrate

create a requirements file for docker, go inside main firstproject folder which have app and project folder then run
pipenv install pipreqs
pipreqs .

create Dockerfile inside the same main project directory
run the below command to create a docker image
docker build . -t first-django-app:latest && docker run -e PYTHONUNBUFFERED=1 -p 8000:8000 first-django-app

to connect docker to the host running postgresql change the localhost to host.docker.internal in the settings.py file in firstapp folder
