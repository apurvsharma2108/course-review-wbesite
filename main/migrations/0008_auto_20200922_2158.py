# Generated by Django 3.0.8 on 2020-09-22 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20200922_2158'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='AverageRating',
            new_name='rating',
        ),
    ]
