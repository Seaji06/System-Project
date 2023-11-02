from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_photo = models.ImageField(upload_to='profile_pics/', default='default.jpg')
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], blank=True)
    birthday = models.DateField(null=True, blank=True)
    contact_number = models.CharField(max_length=15, null=True, blank=True)
    membership_choices = [
        ('no_class', 'No Class'),
        ('beginner_class', 'Beginner Class'),
        ('intermediate_class', 'Intermediate Class'),
        ('master_class', 'Master Class'),
    ]
    membership = models.CharField(max_length=20, choices=membership_choices, default='no_class')

    def __str__(self):
        return self.user.username
