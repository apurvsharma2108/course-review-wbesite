# Generated by Django 3.0.8 on 2020-09-21 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_course_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.URLField(default=None, null=True),
        ),
    ]
