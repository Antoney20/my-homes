# Generated by Django 4.1.5 on 2023-07-27 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myhome', '0008_user_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]