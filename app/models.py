from django.db import models

# Create your models here.


class Kidsform(models.Model):
    Name = models.CharField(max_length=30)
    Email = models.EmailField(max_length=200)
    Hobbies = models.CharField(max_length=30)
    DOB = models.DateField(max_length=8)

    def __str__(self):
        return self.Name
class Adultform(models.Model):
    Name = models.CharField(max_length=30)
    Email = models.EmailField(max_length=200)
    Hobbies = models.CharField(max_length=30)
    DOB = models.DateField(max_length=8)

    def __str__(self):
        return self.Name
