# Generated by Django 4.2.6 on 2023-11-05 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_remove_about_text3_remove_about_text4'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('services_title', models.CharField(max_length=100)),
                ('services_des', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='about',
            old_name='text1',
            new_name='about_des',
        ),
        migrations.RenameField(
            model_name='about',
            old_name='text2',
            new_name='about_title',
        ),
    ]
