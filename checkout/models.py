import uuid

from django.db import models
from django.conf import settings

from guide.models import Patron

# Create your models here.


class PatronUpgrade(models.Model):

    order_number = models.CharField(max_length=32, null=False, editable=False)
    date = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=254, null=False, blank=False)
    country_of_residence = models.CharField(max_length=40, null=False, blank=False)

    def _generate_order_number(self):
        
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.order_number
