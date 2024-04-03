from django.db import models

# Create your models here.

class School(models.Model):
   sname = models.CharField(max_length=100, primary_key=True)
   sprincipal = models.CharField(max_length=100)
   
   def __str__(self):
      return self.sname
   
class Student(models.Model):
   stdname = models.CharField(max_length=50)
   stdpno = models.CharField(max_length=50)
   sname = models.ForeignKey(School,on_delete=models.CASCADE)

   def __str__(self):
      return self.stdname