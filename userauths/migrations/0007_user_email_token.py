# Generated by Django 5.0.6 on 2024-11-19 12:14

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0006_user_email_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email_token',
            field=models.UUIDField(blank=True, default=None, editable=False, null=True, unique=True),
        ),
    ]
