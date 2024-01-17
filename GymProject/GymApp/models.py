from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

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

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    try:
        instance.userprofile.save()
    except UserProfile.DoesNotExist:
        UserProfile.objects.create(user=instance)

class Message(models.Model):
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name

class ClassSchedule(models.Model):
    DAYS_CHOICES = [
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
    ]

    class_name = models.CharField(max_length=255)
    trainer_name = models.CharField(max_length=255)
    day = models.CharField(max_length=10, choices=DAYS_CHOICES)
    time_start = models.TimeField()
    time_end = models.TimeField()

    def __str__(self):
        return self.class_name

    def get_schedule_time(self, day):
        if day == self.day.lower():
            return f'{self.time_start.strftime("%I:%M%p")} - {self.time_end.strftime("%I:%M%p")}'
        else:
            return ''

class Booking(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    class_schedule = models.ForeignKey(ClassSchedule, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user_profile.user.username} - {self.class_schedule.class_name}'