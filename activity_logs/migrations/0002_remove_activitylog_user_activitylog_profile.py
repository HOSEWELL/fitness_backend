# Generated by Django 5.1.3 on 2024-12-02 16:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity_logs', '0001_initial'),
        ('profiles', '0003_alter_profile_age_alter_profile_password_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activitylog',
            name='user',
        ),
        migrations.AddField(
            model_name='activitylog',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.profile'),
        ),
    ]
