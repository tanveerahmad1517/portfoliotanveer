# Generated by Django 2.1.1 on 2018-09-19 08:22

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='get_picture',
            field=cloudinary.models.CloudinaryField(blank=True, default='user.png', max_length=255, null=True, verbose_name='Profile_pictures'),
        ),
    ]
