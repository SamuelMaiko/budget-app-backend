# Generated by Django 5.1.2 on 2024-11-02 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_weekly_budget', '0007_alter_weekitemassociation_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statement',
            name='description',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]