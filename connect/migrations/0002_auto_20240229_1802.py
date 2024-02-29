# Generated by Django 3.2.24 on 2024-02-29 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('connect', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainerreview',
            name='approved',
        ),
        migrations.RemoveField(
            model_name='trainerreview',
            name='date_posted',
        ),
        migrations.AddField(
            model_name='trainerreview',
            name='user_profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='trainer_reviews', to='profiles.userprofile'),
        ),
    ]
