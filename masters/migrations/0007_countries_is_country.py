# Generated by Django 3.2.7 on 2021-10-25 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masters', '0006_alter_countries_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='countries',
            name='is_country',
            field=models.BooleanField(default=True),
        ),
    ]