# Generated by Django 2.1.1 on 2018-09-24 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='created',
            new_name='date',
        ),
    ]