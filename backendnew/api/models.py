from django.db import models
from django.core import serializers
from django.db.models import signals
from django.db.models.signals import post_save
from django.dispatch import receiver
#how to import the USer
from django.contrib.auth.models import User



    
class Common_user(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    phone_number=models.BigIntegerField()
    



# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, unique=True)
    user_type = models.CharField(max_length=10, choices=[('student', 'Student'), ('teacher', 'Teacher')])

    
    def __str__(self):
     
        return self.name
    
    def to_json(self):
        return serializers.serialize('json', [self])
    
class teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, unique=True)
    user_type = models.CharField(max_length=10, choices=[('student', 'Student'), ('teacher', 'Teacher')])

    
    def __str__(self):
        return self.name
    
    def to_json(self):
        return serializers.serialize('json', [self])
    
class course_category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.name

    def to_json(self):
        return serializers.serialize('json', [self])

class video(models.Model):
    course = models.ForeignKey('course', on_delete=models.CASCADE, related_name='videos')
    video = models.FileField(upload_to='videos/')

    def __str__(self):
        return f"Video for course: {self.course.name}"


class course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(course_category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    module  = models.IntegerField()
    def __str__(self):
        return self.name

    def to_json(self):
        return serializers.serialize('json', [self])   





    
class course_enrollement(models.Model):
    student = models.ForeignKey(student, on_delete=models.CASCADE)
    course = models.ForeignKey(course, on_delete=models.CASCADE)
    date_enrolled = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.student.name} enrolled in {self.course.name}"

    def to_json(self):
        return serializers.serialize('json', [self])
