# Generated by Django 5.0.4 on 2024-11-21 11:11

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0008_alter_user_email_token'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlacklistedToken',
            fields=[
                ('token_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('token', models.TextField()),
            ],
        ),
    ]
