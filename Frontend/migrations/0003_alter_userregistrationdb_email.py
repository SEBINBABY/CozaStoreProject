# Generated by Django 4.2.6 on 2023-12-12 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0002_userregistrationdb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userregistrationdb',
            name='EMAIL',
            field=models.EmailField(blank=True, max_length=200, null=True),
        ),
    ]