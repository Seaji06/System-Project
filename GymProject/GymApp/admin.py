from django.contrib import admin
from .models import UserProfile, Message, ClassSchedule, Booking

admin.site.register(UserProfile)
admin.site.register(Message)
admin.site.register(ClassSchedule)
admin.site.register(Booking)