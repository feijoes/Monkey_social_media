# Generated by Django 4.0.2 on 2022-03-16 23:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='datecreate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
