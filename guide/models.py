from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField 
from django.db.models.signals import post_save


class Region(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=50, unique=True)
    region = models.ForeignKey(
        Region, on_delete=models.CASCADE, related_name='country'
        )
    
    def __str__(self):
        return self.name


class Location(models.Model):

    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, related_name='country'
        )
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


class Patron(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True
        )
    patron_status = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

def create_patron(instance, created, **kwargs): 
    if created: Patron.objects.create(user=instance) 

post_save.connect(create_patron, sender=User)


class BookmarkNotes(models.Model):
    bookmark_notes = models.ForeignKey(Location, on_delete=models.CASCADE)
    bookmark_owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username