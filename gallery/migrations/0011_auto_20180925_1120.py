# Generated by Django 2.1.1 on 2018-09-25 11:20

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0010_auto_20180925_0701'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery_category',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gallery_category',
            name='galleryimage',
            field=cloudinary.models.CloudinaryField(default=1, max_length=255, verbose_name='galleryimage'),
            preserve_default=False,
        ),
    ]
