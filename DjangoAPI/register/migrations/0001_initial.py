# Generated by Django 4.0.5 on 2022-07-10 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookingSpace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('room', models.CharField(max_length=10)),
                ('time', models.TimeField()),
                ('date', models.DateField()),
            ],
        ),
    ]