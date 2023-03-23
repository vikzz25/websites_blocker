from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Blocks(models.Model):
    blocked = models.CharField(max_length=122)
    #unblocked = models.CharField(max_length=122)
    date = models.DateField(null=True)

    def __str__(self):
        return self.blocked

class Unblocks(models.Model):
    unblocked = models.CharField(max_length=122)
    date = models.DateField(null=True)
    
    def __str__(self):
        return self.unblocked