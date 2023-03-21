# autopep8: off
# Django specific settings
import inspect
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
from django.db import connection
# Ensure settings are read
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from crud.models import *
from datetime import date


# Your code starts from here:
# Find learners with last name Smith
learner_smith = Learner.objects.filter(last_name='Smith')
print("1. Find learners with last name `Smith`")
print(learner_smith)

# Find two youngest learners (ordered by dob)
# Order by dob descending, and select the first two objects
youngest_learners = Learner.objects.order_by('-dob')[0:2]
print("2. Find top two youngest learners")
print(youngest_learners)