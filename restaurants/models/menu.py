from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from restaurants.models import Restaurant
from restaurants.models.dish import Dish


class Menu(models.Model):
    name = models.CharField(max_length=100)
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name="menus"
    )
    dishes = models.ManyToManyField(Dish, related_name="menus")

    def __str__(self):
        return self.name


class MenuDay(models.Model):
    WEEKDAYS = (
        (1, "Monday"),
        (2, "Tuesday"),
        (3, "Wednesday"),
        (4, "Thursday"),
        (5, "Friday"),
        (6, "Saturday"),
        (7, "Sunday"),
    )

    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name="days")
    day = models.PositiveSmallIntegerField(
        choices=WEEKDAYS, validators=[MinValueValidator(1), MaxValueValidator(7)]
    )

    class Meta:
        unique_together = ("menu", "day")

    @property
    def day_name(self):
        return dict(self.WEEKDAYS).get(self.day)
