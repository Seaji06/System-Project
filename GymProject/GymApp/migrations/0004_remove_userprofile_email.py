# Generated by Django 4.2.6 on 2023-11-02 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GymApp', '0003_userprofile_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='email',
        ),
    ]
