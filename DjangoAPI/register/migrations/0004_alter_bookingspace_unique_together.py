# Generated by Django 4.0.5 on 2022-07-10 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_remove_bookingspace_user'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='bookingspace',
            unique_together={('room', 'time', 'date')},
        ),
    ]