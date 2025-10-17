from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    rating = models.FloatField(validators=[MaxValueValidator(5), MinValueValidator(0)])
    location = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} [rating {self.rating}/5]"
