from django.db import models
from django.contrib.auth.models import User

BELT_CHOICES = [
    ("White", "White"),
    ("Blue", "Blue"),
    ("Purple", "Purple"),
    ("Brown", "Brown"),
    ("Black", "Black"),
]

MATCH_CHOICES = [
    ("WS", "Win by Submission"),
    ("LS", "Loss by Submission"),
    ("WP", "Win by Points"),
    ("LP", "Loss by Points"),
    ("D", "Draw"),
]

# TODO: add functionality so users can add to this list
SUB_CHOICES = [
    ("T", "Triangle"),
    ("A", "Armbar"),
    ("K", "Kimura"),
    ("HH", "Heel Hook"),
    ("AL", "Ankle Lock"),
    ("CC", "Collar Choke"),
    ("None", "None"),
]

# TODO: add functionality to record multiple techniques used
# TODO: add functionality so users can add to the list, maybe have separate lists of sweeps, passes and takedowns?
TECH_CHOICES = [
    ("Sw", "Sweep"),
    ("Pass", "Pass"),
    ("TD", "Takedown"),
]


# Create your models here.
class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    gym = models.CharField(max_length=100)
    belt = models.CharField(max_length=6, choices=BELT_CHOICES, default='white')

    def __str__(self):
        return self.username


class Match(models.Model):
    winner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='matches_won')
    loser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='matches_lost')
    result = models.CharField(max_length=25, choices=MATCH_CHOICES, default='Draw')
    submission = models.CharField(max_length=25, choices=SUB_CHOICES, default='None')
    tech_used = models.CharField(max_length=25, choices=TECH_CHOICES, )
    date = models.DateField()
    notes = models.TextField(blank=True)


# TODO: start adding achievements users can earn
class Achievement(models.Model):
    name = models.CharField(max_length=100)

