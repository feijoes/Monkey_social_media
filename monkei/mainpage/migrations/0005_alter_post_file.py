# Generated by Django 4.0.2 on 2022-03-20 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0004_alter_profile_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
