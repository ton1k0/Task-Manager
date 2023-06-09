# Generated by Django 4.1.7 on 2023-04-11 19:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0008_alter_company_code_alter_company_code_expiration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='code',
            field=models.CharField(default='4903f68d1a5f49d585dd87b93ea3b85b', max_length=8, unique=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='code_expiration',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 18, 19, 18, 51, 559322, tzinfo=datetime.timezone.utc)),
        ),
    ]
