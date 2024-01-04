# Generated by Django 4.2.6 on 2023-12-10 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0002_prodcutdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DATE', models.DateField(blank=True, null=True)),
                ('TITLE', models.CharField(blank=True, max_length=100, null=True)),
                ('SHORTDESC', models.CharField(blank=True, max_length=200, null=True)),
                ('FULLDESC', models.CharField(blank=True, max_length=800, null=True)),
                ('IMAGE', models.ImageField(blank=True, null=True, upload_to='Images')),
            ],
        ),
    ]
