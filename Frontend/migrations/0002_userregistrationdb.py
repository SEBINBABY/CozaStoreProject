# Generated by Django 4.2.6 on 2023-12-11 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRegistrationDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NAME', models.CharField(blank=True, max_length=100, null=True)),
                ('EMAIL', models.EmailField(blank=True, max_length=200, null=True, unique=True)),
                ('PASSWORD', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]