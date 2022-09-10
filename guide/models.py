from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField 

class Location(models.Model):

    COUNTRY_CHOICES = [
        ('BE', 'Belize'),
        ('CR', 'Costa Rica'),
        ('ES', 'El Salvador'),
        ('GU', 'Guatemala'),
        ('HO', 'Honduras'),
        ('NI', 'Nicaragua'),
        ('PA', 'Panama')
    ]

    REGION_CHOICES = [
        ('CA', 'Central America')
    ]

    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    country = models.CharField(choices=COUNTRY_CHOICES)
    region = models.CharField(choices=REGION_CHOICES)
    content = models.TextField(blank=True)
    bookmarks = models.ManyToManyField(
        User, related_name='location_bookmark', blank=True
    )
    map_image = CloudinaryField('image', default='placeholder')
    landscape_image = CloudinaryField('image', default='placeholder')
    feature_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.title

