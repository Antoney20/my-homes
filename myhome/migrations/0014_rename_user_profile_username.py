# Generated by Django 4.1.5 on 2023-07-27 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myhome', '0013_profile_phone_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user',
            new_name='username',
        ),
    ]
