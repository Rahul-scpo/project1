from django.db import models

# Create your models here.
class logintable(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    Type=models.CharField(max_length=100)
    def __str__(self):
        return self.Name


class usertable(models.Model):
    Loginid = models.ForeignKey(logintable, on_delete=models.CASCADE, default=1)
    Name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    Type = models.CharField(max_length=100)
    def __str__(self):
        return self. Name

class personaltable(models.Model):
    Name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.IntegerField()
    address=models.CharField(max_length=400)
    Email = models.EmailField()
    number = models.IntegerField()
    Type = models.CharField(max_length=150)
    def __str__(self):
        return self.Name