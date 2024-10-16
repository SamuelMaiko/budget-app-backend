# Generated by Django 5.1.2 on 2024-10-16 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_wallet', '0002_rename_user_transaction_wallet_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='wallet',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
