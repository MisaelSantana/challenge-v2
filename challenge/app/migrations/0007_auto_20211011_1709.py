# Generated by Django 2.2.24 on 2021-10-11 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20211011_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='UPDATED',
            field=models.IntegerField(),
        ),
    ]
