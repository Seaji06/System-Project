# Generated by Django 4.2.7 on 2024-01-17 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GymApp', '0006_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=255)),
                ('trainer_name', models.CharField(max_length=255)),
                ('day', models.CharField(choices=[('monday', 'Monday'), ('tuesday', 'Tuesday'), ('wednesday', 'Wednesday'), ('thursday', 'Thursday'), ('friday', 'Friday')], max_length=10)),
                ('time_start', models.TimeField()),
                ('time_end', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_date', models.DateTimeField(auto_now_add=True)),
                ('class_schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GymApp.classschedule')),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GymApp.userprofile')),
            ],
        ),
    ]
