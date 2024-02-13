# Generated by Django 5.0.1 on 2024-02-07 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=100)),
                ('license_no', models.CharField(max_length=20)),
                ('seen', models.BooleanField(default=False)),
            ],
        ),
    ]
