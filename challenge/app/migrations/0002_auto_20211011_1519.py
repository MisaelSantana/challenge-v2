# Generated by Django 2.2.24 on 2021-10-11 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='locations',
            old_name='pt_chegada',
            new_name='PT_CHEGADA',
        ),
        migrations.RenameField(
            model_name='locations',
            old_name='pt_partida',
            new_name='PT_PARTIDA',
        ),
        migrations.AddField(
            model_name='locations',
            name='ID_LOCALIZACAO',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.Location'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='locations',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
