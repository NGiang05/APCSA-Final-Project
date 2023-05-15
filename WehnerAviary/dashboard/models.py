from django.db import models

# Create your models here.
class CircuitEntry(models.Model):
    name = models.CharField(max_length=255)
    period = models.IntegerField()
    circuit_completed = models.IntegerField()
