# autopep8: off
# Django specific settings
import inspect
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
from django.db import connection

# Ensure settings are read
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from datetime import date
from crud.models import *


# Your code starts from here:
courses = Course.objects.all()
print(courses)
