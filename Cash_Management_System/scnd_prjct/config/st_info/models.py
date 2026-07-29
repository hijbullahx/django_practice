from django.db import models

# Create your models here.
class Student(models.Model):
    st_id = models.IntegerField("max_length = 20, unique = True")
    st_name = models.CharField(max_length=100)
    dept = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    address = models.TextField()
    def __str__(self):
        return f"{self.st_id} - {self.st_name}"

