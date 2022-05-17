from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    age = models.IntegerField(blank=False, null=False)
    address = models.CharField(max_length=300, blank=False, null=False)
