# Generated by Django 3.2.7 on 2021-10-28 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masters', '0007_countries_is_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='continent',
            name='images',
            field=models.ImageField(default='', upload_to='images'),
            preserve_default=False,
        ),
    ]