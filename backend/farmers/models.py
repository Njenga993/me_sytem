# yourapp/models.py
from django.db import models
from .fields import EncryptedCharField

class Farmer(models.Model):
    name = models.CharField(max_length=100)
    national_id = EncryptedCharField(max_length=500)
    phone = EncryptedCharField(max_length=500)

    def __str__(self):
        return self.name
