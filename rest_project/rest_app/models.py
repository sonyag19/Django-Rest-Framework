from django.db import models

# Create your models here.
class todos(models.Model):
    taskname=models.CharField(max_length=50)
    user=models.CharField(max_length=50)
    status=models.BooleanField(default=False)

class Mobile(models.Model):
    mobileName=models.CharField(max_length=20)
    mobileModel=models.CharField(max_length=20)
    ram=models.IntegerField()
    storage=models.IntegerField()
    color=models.CharField(max_length=20)

class MixinModel(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.IntegerField()

class EmployeeModel(models.Model):
    name=models.CharField(max_length=20)
    salary=models.IntegerField()
    department=models.CharField(max_length=20)
    designation=models.CharField(max_length=20)
    company=models.CharField(max_length=20)

class carModel(models.Model):
    Car_name=models.CharField(max_length=20)
    model=models.CharField(max_length=20)
    engine=models.CharField(max_length=20)
    owners_name=models.CharField(max_length=20)

class MovieModel(models.Model):
    movie_name=models.CharField(max_length=50)
    no_of_seats=models.IntegerField()
    streaming_time=models.CharField(max_length=20)
    streaming_date=models.DateField()
    Theatre_name=models.CharField(max_length=30)

class PersonModel(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    age=models.IntegerField()
    phone=models.IntegerField()




