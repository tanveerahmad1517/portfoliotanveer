# Generated by Django 2.1.1 on 2018-09-25 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0009_artwork_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artwork',
            old_name='category',
            new_name='gcategory',
        ),
    ]
