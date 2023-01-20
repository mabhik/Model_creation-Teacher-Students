from django.db import models

# Create your models here.
class Teacher(models.Model):
    Tid=models.IntegerField()
    Name=models.CharField(max_length=30)
    Subject=models.CharField(max_length=40)

    def __str__(self):
        return self.Subject

class Student(models.Model):
    Sid=models.IntegerField()
    SName=models.CharField(max_length=40)
    Subject=models.ForeignKey(Teacher, on_delete=models.CASCADE)

