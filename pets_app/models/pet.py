from django.db import models
from .owner import Owner

class Pet(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    age = models.IntegerField()
    owner = models.ForeignKey(Owner, related_name='pets', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
