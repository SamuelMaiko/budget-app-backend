# Generated by Django 5.1.2 on 2024-11-02 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('a_weekly_budget', '0006_alter_week_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='weekitemassociation',
            options={'ordering': ('-created_at',)},
        ),
    ]