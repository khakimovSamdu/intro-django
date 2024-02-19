from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    age = models.TextField()
    

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name + " " + self.age
    
class Human(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    country = models.TextField()
    language = models.TextField()
    def __str__(self) -> str:
        return self.first_name + "\n" + self.last_name + "\n" + self.country + "\n" + self.language
    
class Student(models.Model):
    ism = models.TextField()
    fam = models.TextField()
    yosh = models.TextField()
    yonalish = models.TextField()
    kurs = models.TextField()
    def __str__(self) :
        return self.ism +" "+ self.fam + " " + self.yosh + " " + self.yonalish +" " + self.kurs 