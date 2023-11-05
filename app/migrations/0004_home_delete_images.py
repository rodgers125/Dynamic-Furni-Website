# Generated by Django 4.2.6 on 2023-11-03 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text1', models.CharField(max_length=100)),
                ('text2', models.CharField(max_length=100)),
                ('all_images', models.ImageField(default='profile.png', upload_to='images')),
            ],
        ),
        migrations.DeleteModel(
            name='Images',
        ),
    ]