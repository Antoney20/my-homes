# Generated by Django 4.1.5 on 2023-07-27 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myhome', '0009_alter_user_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='slug',
        ),
    ]
