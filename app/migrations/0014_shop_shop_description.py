# Generated by Django 4.2.6 on 2023-11-03 19:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_shop'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='shop_description',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
