# Generated by Django 5.0.4 on 2024-10-11 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='profile_image',
            new_name='profile_image_url',
        ),
    ]