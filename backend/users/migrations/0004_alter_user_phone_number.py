# Generated by Django 4.0.10 on 2024-08-11 16:18

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='VN'),
        ),
    ]
