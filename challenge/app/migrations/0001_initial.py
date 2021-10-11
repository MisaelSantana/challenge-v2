# Generated by Django 2.2.24 on 2021-10-11 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_DATA', models.IntegerField()),
                ('ID_LOCALIZACAO', models.CharField(max_length=10)),
                ('KMPER_40KM', models.CharField(max_length=10)),
                ('KMPER_60KM', models.CharField(max_length=10)),
                ('KMPER_80KM', models.CharField(max_length=10)),
                ('KMPER_100KM', models.CharField(max_length=10)),
                ('COSM_40KM', models.CharField(max_length=10)),
                ('COSM_60KM', models.CharField(max_length=10)),
                ('COSM_80KM', models.CharField(max_length=10)),
                ('COSM_100KM', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_LOCALIZACAO', models.IntegerField()),
                ('PT_PARTIDA', models.CharField(max_length=10)),
                ('PT_CHEGADA', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('pt_partida', models.CharField(max_length=255)),
                ('pt_chegada', models.CharField(max_length=255)),
                ('createdAt', models.DateField(max_length=10)),
                ('updated', models.DateField(max_length=10)),
            ],
        ),
    ]
