from django.db import models


class Newsletter(models.Model):
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.email
