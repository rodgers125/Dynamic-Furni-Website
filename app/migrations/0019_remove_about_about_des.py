# Generated by Django 4.2.6 on 2023-11-05 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_remove_services_services_des'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='about_des',
        ),
    ]
