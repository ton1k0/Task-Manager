# Generated by Django 4.1.8 on 2023-04-27 18:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0015_alter_company_code_alter_company_code_expiration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='code',
            field=models.CharField(default='f799514ee56c438da9fb9249342fafa0', max_length=8, unique=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='code_expiration',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 4, 18, 35, 1, 266116, tzinfo=datetime.timezone.utc)),
        ),
    ]
