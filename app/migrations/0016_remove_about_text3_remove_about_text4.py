# Generated by Django 4.2.6 on 2023-11-05 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_about'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='text3',
        ),
        migrations.RemoveField(
            model_name='about',
            name='text4',
        ),
    ]
