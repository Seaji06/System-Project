# Generated by Django 4.2.6 on 2023-11-02 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GymApp', '0002_userprofile_first_name_userprofile_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
