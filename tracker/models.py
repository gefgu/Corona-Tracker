from django.db import models

# Create your models here.
class Case(models.Model):
    confirmed = models.BooleanField()
