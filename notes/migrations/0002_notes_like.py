# Generated by Django 5.2 on 2025-04-21 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='like',
            field=models.IntegerField(default=0),
        ),
    ]
