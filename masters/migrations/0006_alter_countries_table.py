# Generated by Django 3.2.7 on 2021-10-23 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('masters', '0005_countries'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='countries',
            table='country_master',
        ),
    ]
