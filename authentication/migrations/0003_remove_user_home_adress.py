# Generated by Django 4.1 on 2022-10-13 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_remove_user_numbers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='home_adress',
        ),
    ]
