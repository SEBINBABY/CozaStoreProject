# Generated by Django 4.2.7 on 2024-01-16 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0006_checkoutdb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartdbsave',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='checkoutdb',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='contactdb',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='userregistrationdb',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
