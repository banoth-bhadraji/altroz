# Generated by Django 3.2.7 on 2021-10-23 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masters', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='continent',
            name='notes',
            field=models.TextField(default=''),
        ),
    ]
