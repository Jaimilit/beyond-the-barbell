# Generated by Django 3.2.24 on 2024-02-22 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0002_trainerreview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainerreview',
            name='rating',
            field=models.IntegerField(choices=[(1, '1 star'), (2, '2 stars'), (3, '3 stars'), (4, '4 stars'), (5, '5 stars')]),
        ),
    ]
