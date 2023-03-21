from django.db import models
from django.utils.timezone import now


class User(models.Model):
    # User model
    first_name = models.CharField(null=False, max_length=30, default='john')
    last_name = models.CharField(null=False, max_length=30, default='doe')
    dob = models.DateField(null=True)

    # Create a toString method for object string representation
    def __str__(self):
        return self.first_name + " " + self.last_name


class Instructor(User):
    # Instructor model model inherited from User model and make it as One-To-One relationship
    full_time = models.BooleanField(default=True)
    total_learners = models.IntegerField()

    # Create a toString method for object string representation
    def __str__(self):
        return "First name: " + self.first_name + ", " + \
               "Last name: " + self.last_name + ", " + \
               "Is full time: " + str(self.full_time) + ", " + \
               "Total Learners: " + str(self.total_learners)


class Learner(User):
    # Learner model inherited from User with some learner related fields
    STUDENT = 'student'
    DEVELOPER = 'developer'
    DATA_SCIENTIST = 'data_scientist'
    DATABASE_ADMIN = 'dba'
    OCCUPATION_CHOICES = [
        (STUDENT, 'Student'),
        (DEVELOPER, 'Developer'),
        (DATA_SCIENTIST, 'Data Scientist'),
        (DATABASE_ADMIN, 'Database Admin')
    ]
    # Occupation Char field with defined enumeration choices
    occupation = models.CharField(
        null=False,
        max_length=20,
        choices=OCCUPATION_CHOICES,
        default=STUDENT
    )
    # Social link URL field
    social_link = models.URLField(max_length=200)

    # Create a toString method for object string representation
    def __str__(self):
        return "First name: " + self.first_name + ", " + \
            "Last name: " + self.last_name + ", " \
            "Date of Birth: " + str(self.dob) + ", " + \
            "Occupation: " + self.occupation + ", " + \
            "Social Link: " + self.social_link


class Course(models.Model):
    # Course model which has a Many-To-Many relationship to Instructor model
    name = models.CharField(null=False, max_length=100,
                            default='online course')
    description = models.CharField(max_length=500)
    # Many-To-Many relationship with Instructor
    instructors = models.ManyToManyField(Instructor)
    # Many-To-Many relationship with Learner via Enrollment relationship
    learners = models.ManyToManyField(Learner, through='Enrollment')

    # Create a toString method for object string representation
    def __str__(self):
        return "Name: " + self.name + "," + \
            "Description: " + self.description


class Lesson(models.Model):
    # Lesson A course normally contains several lessons thus has a One-To-Many relationship to a Lesson model
    title = models.CharField(max_length=200, default="title")
    course = models.ForeignKey(Course, null=True, on_delete=models.CASCADE)
    content = models.TextField()


class Enrollment(models.Model):
    # Enrollment model as a lookup table with additional enrollment info
    AUDIT = 'audit'
    HONOR = 'honor'
    COURSE_MODES = [
        (AUDIT, 'Audit'),
        (HONOR, 'Honor'),
    ]
    # Add a learner foreign key
    learner = models.ForeignKey(Learner, on_delete=models.CASCADE)
    # Add a course foreign key
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    # Enrollment date
    date_enrolled = models.DateField(default=now)
    # Enrollment mode
    mode = models.CharField(max_length=5, choices=COURSE_MODES, default=AUDIT)
