# Generated by Django 3.2.15 on 2022-11-18 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0010_auto_20221118_1725'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='feature_image',
            new_name='image',
        ),
        migrations.RemoveField(
            model_name='location',
            name='landscape_image',
        ),
        migrations.RemoveField(
            model_name='location',
            name='map_image',
        ),
    ]
