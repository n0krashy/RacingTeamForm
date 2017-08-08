from django.db import models
from django.utils import timezone


class RacingTeamAddUser(models.Model):
    Name = models.CharField(max_length=70)
    Email = models.EmailField(unique=True)
    Phone = models.BigIntegerField(unique=True)
    Age = models.PositiveSmallIntegerField(blank=True)
    MALE = 'M'
    FEMALE = 'F'
    gender_choices = ((MALE, 'Male'), (FEMALE, 'Female'))
    Gender = models.CharField(max_length=2, choices=gender_choices, blank=True)
    Comment = models.TextField(blank=True)