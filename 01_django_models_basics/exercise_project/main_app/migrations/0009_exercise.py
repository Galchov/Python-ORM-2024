# Generated by Django 5.0.4 on 2024-10-11 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_userprofile_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('difficulty_level', models.CharField(max_length=20)),
                ('duration_minutes', models.PositiveIntegerField()),
                ('equipment', models.CharField(max_length=90)),
                ('video_url', models.URLField()),
                ('calories_burnt', models.PositiveIntegerField(default=1)),
                ('is_favorite', models.BooleanField(default=False)),
            ],
        ),
    ]
