# Generated by Django 2.1.1 on 2018-09-24 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]