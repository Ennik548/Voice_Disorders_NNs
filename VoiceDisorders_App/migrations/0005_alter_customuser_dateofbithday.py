# Generated by Django 4.2 on 2023-05-22 13:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VoiceDisorders_App', '0004_alter_customuser_dateofbithday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='dateOfBithday',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 22, 18, 37, 49, 503965)),
        ),
    ]
