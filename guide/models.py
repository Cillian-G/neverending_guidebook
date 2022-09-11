from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField 


class Region(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

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

    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    country = models.CharField(max_length=50, choices=COUNTRY_CHOICES)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    bookmarks = models.ManyToManyField(
        User, related_name='location_bookmark', blank=True
    )
    map_image = CloudinaryField('image', default='placeholder')
    landscape_image = CloudinaryField('image', default='placeholder')
    feature_image = CloudinaryField('image', default='placeholder')
    preview = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Newsletter(models.Model):
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.email


class Contact(models.Model):

    SUBJECT_CHOICES = [
        ('account_issues', 'request help with your account'),
        ('submission_request', 'writing for us'),
        ('correction_request', 'correct one of our location listings'),
        ('location_request', 'suggest an location for us to visit'),
        ('non_cateorized', 'other purposes')
    ]

    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    subject = models.CharField(max_length=20, choices=SUBJECT_CHOICES)
    message = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.name


class Patron(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    patron_status = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

