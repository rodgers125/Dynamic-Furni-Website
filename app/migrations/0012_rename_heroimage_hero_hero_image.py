# Generated by Django 4.2.6 on 2023-11-03 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_rename_image_url_hero_heroimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hero',
            old_name='heroimage',
            new_name='hero_image',
        ),
    ]
