# Generated by Django 4.2.6 on 2023-12-11 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0003_blogdb'),
    ]

    operations = [
        migrations.AddField(
            model_name='prodcutdb',
            name='PROIMAGE2',
            field=models.ImageField(blank=True, null=True, upload_to='Images'),
        ),
    ]
