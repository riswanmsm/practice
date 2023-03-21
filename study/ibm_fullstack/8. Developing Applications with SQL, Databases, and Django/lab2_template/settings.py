# Postgre SQL
import os
from dotenv import load_dotenv

# Loading env file to get the sensitive data
load_dotenv()
# assigning postgress password from the env file
postgres_pass = os.environ['postgres_pass']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'root',
        'PASSWORD': postgres_pass,
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

INSTALLED_APPS = (
    'crud',
)

SECRET_KEY = 'SECRET KEY for this Django Project'
