# Generated by Django 3.1.8 on 2023-12-30 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0004_auto_20231228_0140'),
    ]

    operations = [
        migrations.CreateModel(
            name='cartdbsave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(blank=True, max_length=20, null=True)),
                ('usrname', models.CharField(blank=True, max_length=100, null=True)),
                ('prodname', models.CharField(blank=True, max_length=100, null=True)),
                ('qnty', models.IntegerField(blank=True, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('totalprice', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]