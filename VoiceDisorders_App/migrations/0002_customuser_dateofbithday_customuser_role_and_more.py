# Generated by Django 4.2 on 2023-05-21 17:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VoiceDisorders_App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='dateOfBithday',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 21, 22, 33, 27, 398039)),
        ),
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customuser',
            name='sex',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='surname',
            field=models.CharField(max_length=30),
        ),
    ]