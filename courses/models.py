from django.db import models
from coaches.models import Coach

class Course(models.Model):
    name = models.CharField(max_length=200)    
    short_description = models.CharField(max_length=255, null = True, blank=True)
    description = models.TextField(null = True, blank=True)
    coach = models.ForeignKey(Coach, related_name='coach_courses', 
                              null = True, blank=True)
    assistant = models.ForeignKey(Coach, related_name='assistant_courses',
                                  null = True, blank=True)

    def __str__(self):
        return self.name

class Lesson(models.Model):
    subject = models.CharField(max_length=200)
    description = models.TextField(null = True, blank=True)
    course = models.ForeignKey(Course)
    order = models.PositiveIntegerField()    

    def __str__(self):
        return self.subject



    class Meta:
        ordering = ['order']

# Create your models here.
