from django.db import models
from django.contrib.auth.models import User

BELT_CHOICES = [
    ("White", "White"),
    ("Blue", "Blue"),
    ("Purple", "Purple"),
    ("Brown", "Brown"),
    ("Black", "Black"),
]


# Create your models here.
class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    belt = models.CharField(max_length=6, choices=BELT_CHOICES, default='white')

    def __str__(self):
        return self.username


class Match(models.Model):
    winner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='matches_won')
    loser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='matches_lost')
    date = models.DateField()
    notes = models.TextField(blank=True)



