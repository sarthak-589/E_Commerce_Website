# Generated by Django 5.0.3 on 2024-04-01 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_rename_paymnet_type_payment_payment_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='payment_status',
            field=models.CharField(choices=[('Paid', 'Paid'), ('Not Paid', 'Not Paid')], default='Not Paid', max_length=30),
        ),
    ]
