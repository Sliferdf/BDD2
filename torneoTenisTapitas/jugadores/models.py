from django.db import models

# Create your models here.
class jugadores(models.Model):
    nombre = models.CharField(max_length=50);
    edad = models.IntegerField();
    ranking = models.IntegerField();
    nacionalidad = models.CharField(max_length=50);
    estatura = models.CharField(max_length=10);
    peso = models.IntegerField();
    debut = models.IntegerField();
 