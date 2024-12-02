# Generated by Django 5.1.3 on 2024-12-02 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='goal_type',
            field=models.CharField(choices=[('cardio', 'Cardio'), ('strength', 'Strength'), ('steps', 'Steps'), ('workout', 'Workout'), ('flexibility', 'Flexibility')], max_length=20),
        ),
    ]