# Generated by Django 4.1.5 on 2023-07-27 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myhome', '0012_alter_user_options_alter_user_managers_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=12),
        ),
    ]
