from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)

class Match(models.Model):
    home_team = models.CharField(max_length=255)
    guest_team = models.CharField(max_length=255)
    winner = models.CharField(max_length=255)
    score_parties = models.CharField(max_length=255)