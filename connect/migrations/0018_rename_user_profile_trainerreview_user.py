# Generated by Django 3.2.24 on 2024-02-29 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0017_auto_20240229_1113'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trainerreview',
            old_name='user_profile',
            new_name='user',
        ),
    ]