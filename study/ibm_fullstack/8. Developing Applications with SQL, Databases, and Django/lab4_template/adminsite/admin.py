from django.contrib import admin
from .models import Course, Instructor, Lesson

# Register your models here.


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5


class CustomCourseAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'name', 'description']
    inlines = [LessonInline]


class CustomInstructorAdmin(admin.ModelAdmin):
    fields = ['user', 'full_time']


admin.site.register(Course, CustomCourseAdmin)
admin.site.register(Instructor, CustomInstructorAdmin)
