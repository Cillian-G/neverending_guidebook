from django.db import models
from django.conf import settings

from guide.models import Patron

# Create your models here.


class PatronUpgrade(models.Model):

    date = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=254, null=False, blank=False)