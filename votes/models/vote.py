from django.contrib.auth import get_user_model
from django.db import models

from restaurants.models import Restaurant

User = get_user_model()


class Vote(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="votes")
    vote_date = models.DateField()

    class Meta:
        unique_together = ("restaurant", "vote_date")
        ordering = ["-vote_date"]


class VoteItem(models.Model):
    CHOICES = (
        (True, "For"),
        (False, "Against")
    )
    vote = models.ForeignKey(Vote, on_delete=models.CASCADE, related_name="items")
    employee = models.ForeignKey(User, on_delete=models.CASCADE, related_name="vote_items")
    choice = models.BooleanField(choices=CHOICES)

    class Meta:
        unique_together = ("vote", "employee")
