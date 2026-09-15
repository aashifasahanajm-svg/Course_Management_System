
from django.db import models

class Course(models.Model):
    course_id = models.CharField(max_length=20, unique=True)
    course_name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)
    duration = models.IntegerField()

    def __str__(self):
        return self.course_name