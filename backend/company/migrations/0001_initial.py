# Generated by Django 4.1.8 on 2023-04-07 15:28

import datetime
from django.conf import settings
from django.db import migrations, models
import secrets


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('web_site', models.TextField(max_length=200)),
                ('code', models.CharField(default=secrets.token_urlsafe, max_length=8, unique=True)),
                ('code_expiration', models.DateTimeField(default=datetime.datetime(2023, 4, 14, 15, 28, 28, 820597, tzinfo=datetime.timezone.utc))),
                ('owners', models.ManyToManyField(related_name='owners_company', to=settings.AUTH_USER_MODEL)),
                ('staff', models.ManyToManyField(related_name='staff_company', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]