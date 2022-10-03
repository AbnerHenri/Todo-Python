from secrets import choice
from telnetlib import STATUS
from turtle import done
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Task(models.Model):

    STATUS = (
        (1, 'Doing'),
        (2, 'Done')
    )

    title = models.CharField(_MAX_LENGTH=255)
    description = models.TextField()
    done = models.CharField(_MAX_LENGTH=1, choices=STATUS)