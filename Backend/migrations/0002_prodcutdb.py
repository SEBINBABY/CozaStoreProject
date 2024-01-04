# Generated by Django 4.2.6 on 2023-12-02 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProdcutDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CATEGORY', models.CharField(blank=True, max_length=100, null=True)),
                ('PRONAME', models.CharField(blank=True, max_length=100, null=True)),
                ('PROPRICE', models.CharField(blank=True, max_length=100, null=True)),
                ('PRODESC', models.CharField(blank=True, max_length=100, null=True)),
                ('PROIMAGE', models.ImageField(blank=True, null=True, upload_to='Images')),
            ],
        ),
    ]