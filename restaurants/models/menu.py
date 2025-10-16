from django.contrib.postgres.fields import ArrayField
from django.db import models

from restaurants.models import Restaurant
from restaurants.models.dish import Dish


class Menu(models.Model):
    WEEKDAYS = (
        (1, "Monday"),
        (2, "Tuesday"),
        (3, "Wednesday"),
        (4, "Thursday"),
        (5, "Friday"),
        (6, "Saturday"),
        (7, "Sunday"),
    )

    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name="menus"
    )
    dishes = models.ManyToManyField(Dish, related_name="menus")
    week_days = ArrayField(
        models.IntegerField(choices=WEEKDAYS),
        default=list,
        help_text="List of days this menu applies to",
    )

    def __str__(self):
        days = ", ".join(str(d) for d in self.week_days)
        return f"{self.restaurant.name} ({days})"
