# Generated by Django 4.2.6 on 2023-11-03 17:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_home_delete_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='text3',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
