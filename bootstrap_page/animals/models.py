from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator, MaxLengthValidator, MinValueValidator
import datetime

# Create your models here.
ANIMAL_CHOICES = (
    ('Perro', 'PERRO'),
    ('Gato', 'GATO')
)

AGE_CHOICES = (
    ('Joven', 'JOVEN'),
    ('Adulto', 'ADULTO'),
    ('Mayor', 'MAYOR')
)

GENDER_CHOICES = (
    ('Macho', 'MACHO'),
    ('Hembra', 'HEMBRA')
)


class Animal(models.Model):
    name = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    image = models.ImageField(upload_to="media/")
    description = models.TextField(max_length=360)
    difficulty = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    animal = models.CharField(choices=ANIMAL_CHOICES, max_length=6)
    age = models.CharField(choices=AGE_CHOICES, max_length=6)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=7)
    sheltered = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.name
