# Generated by Django 2.1.1 on 2018-09-24 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20180924_0725'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-date',), 'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
        migrations.AlterModelOptions(
            name='posttranslation',
            options={'default_permissions': (), 'managed': True, 'verbose_name': 'Post Translation'},
        ),
    ]