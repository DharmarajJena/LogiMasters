# Generated by Django 5.0.2 on 2024-02-15 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fleet', '0002_alter_notifications_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notifications',
            old_name='license_no',
            new_name='registration_no',
        ),
    ]
