from tkinter import CASCADE

from django.db import models
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator
from django.forms import ValidationError


# Create your models here.
def MailVal(Value):
    if not str(Value).endswith('@esprit.tn'):
        raise ValidationError('your email must be @esprit.tn',
        params={'value': Value})
    return Value
   
class User(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(verbose_name="Email",null=False,validators=[MailVal]) #de base charfield

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

class Student(User):
    pass

class Coach(User):
    pass

class Project(models.Model):
    project_name=models.CharField(max_length=50)
    duree=models.IntegerField(default=0)
    temp_alloue=models.IntegerField(validators=[
        MinValueValidator(1,"le temps min doit etre 1 heure"),
        MaxValueValidator(20,"le temps max doit etre 20 heure")
        ])
    besoin=models.TextField(max_length=250)
    description=models.TextField(max_length=250)
    isvalid=models.BooleanField(default=False)
    creator=models.OneToOneField(
        Student,
        on_delete=models.CASCADE,
        related_name="creators"
    )
    supervisor=models.ForeignKey(
        Coach,
        on_delete=models.CASCADE, # en cas ou on supprime le user l'attribute va etre null
        related_name='supervisors'
    )

    members=models.ManyToManyField(
        Student,
        through='MembreShip', #creer manuelement la table intermediaire
        related_name='membres'        
    )
    def __str__(self) -> str:
        return f"{self.project_name}"


class MembreShip(models.Model):
    project=models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='membreships'
    )
    student=models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='students'
        
    )
    allocated_time_by_member=models.IntegerField(default=0)
