# Generated by Django 3.2.24 on 2024-02-29 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('connect', '0012_alter_trainerreview_user_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainerreview',
            name='user_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trainer_reviews', to='profiles.userprofile'),
        ),
    ]
