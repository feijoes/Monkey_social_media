# Generated by Django 4.0.2 on 2022-03-24 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0002_alter_profile_options_alter_profile_user_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='gmail',
        ),
    ]