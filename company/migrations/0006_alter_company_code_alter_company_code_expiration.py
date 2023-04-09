# Generated by Django 4.1.8 on 2023-04-09 08:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_alter_company_code_alter_company_code_expiration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='code',
            field=models.CharField(default='514d97ad2a454f95ac0687b17587488b', max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='code_expiration',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 16, 8, 36, 59, 321682, tzinfo=datetime.timezone.utc)),
        ),
    ]
