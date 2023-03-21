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
def write_instructors():
    # Create User
    user = User(first_name='Riswan', last_name='Saheed', dob=date(1986, 6, 12))
    user.save()

    # Update the user reference of instructor_riswan to be user
    instructor_riswan = Instructor(full_time=True, total_learners=30050)
    instructor_riswan.user = user
    instructor_riswan.save()

    instructors = [
        {'first_name': 'Yan', 'last_name': 'Luo', 'dob': date(
            1962, 7, 16), 'full_time': True, 'total_learners': 30050},
        {'first_name': 'Joy', 'last_name': 'Li', 'dob': date(
            1992, 1, 2), 'full_time': False, 'total_learners': 10040},
        {'first_name': 'Peter', 'last_name': 'Chen', 'dob': date(
            1982, 5, 2), 'full_time': True, 'total_learners': 2002},
    ]

    for instructor in instructors:
        instructor_instance = Instructor(first_name=instructor['first_name'], last_name=instructor['last_name'],
                                         dob=instructor['dob'], full_time=instructor['full_time'], total_learners=instructor['total_learners'])
        instructor_instance.save()
    print('All instructores objects saved')


def write_courses():
    courses = [
        Course(name="Cloud Application Development with Database",
               description="Develop and deploy application on cloud"),
        Course(name="Introduction to Python",
               description="Learn core concepts of Python and obtain hands-on "
               "experience via a capstone project")
    ]

    for course in courses:
        course.save()

    print('Course objects all saved...')


def write_lessons():
    lessons = [
        Lesson(title='Lesson 1', content="Object-relational mapping project"),
        Lesson(title='Lesson 2', content="Django full stack project")
    ]

    for lesson in lessons:
        lesson.save()

    print('Lesson objects all saved...')

def write_learners():
    learners = [
        Learner(first_name='James', last_name='Smith', dob=date(1982, 7, 16),
                            occupation='data_scientist',
                            social_link='https://www.linkedin.com/james/'),
        Learner(first_name='Mary', last_name='Smith', dob=date(1991, 6, 12), occupation='dba',
                           social_link='https://www.facebook.com/mary/'),
        Learner(first_name='Robert', last_name='Lee', dob=date(1999, 1, 2), occupation='student',
                             social_link='https://www.facebook.com/robert/'),
        Learner(first_name='David', last_name='Smith', dob=date(1983, 7, 16),
                            occupation='developer',
                            social_link='https://www.linkedin.com/david/'),
        Learner(first_name='John', last_name='Smith', dob=date(1986, 3, 16),
                           occupation='developer',
                           social_link='https://www.linkedin.com/john/')                    
    ]

    for learner in learners:
        learner.save()

    print('Leaner objects all saved...')
def clean_data():
    # Delete all data to start from fresh
    Enrollment.objects.all().delete()
    User.objects.all().delete()
    Learner.objects.all().delete()
    Instructor.objects.all().delete()
    Course.objects.all().delete()
    Lesson.objects.all().delete()


# Clean any existing data first
clean_data()
# write data to db
write_courses()
write_instructors()
write_lessons()
write_learners()
