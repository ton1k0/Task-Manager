# Generated by Django 4.1.8 on 2023-04-24 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0014_alter_company_code_alter_company_code_expiration'),
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='company_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='company_project', to='company.company'),
        ),
    ]
