# Generated by Django 4.1.8 on 2023-04-07 16:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='code_expiration',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 14, 16, 10, 29, 271210, tzinfo=datetime.timezone.utc)),
        ),
    ]
