# Generated by Django 5.0.4 on 2024-06-11 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='profile_image',
        ),
    ]
