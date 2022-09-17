from django.db import models

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