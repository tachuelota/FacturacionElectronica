# Generated by Django 2.0.6 on 2018-09-09 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0027_auto_20180905_2043'),
    ]

    operations = [
        migrations.AddField(
            model_name='comprobantecab',
            name='nom_archivo',
            field=models.TextField(blank=True, db_column='NOM_ARCHIVO', null=True),
        ),
        migrations.AddField(
            model_name='resumencab',
            name='nom_archivo',
            field=models.TextField(blank=True, db_column='NOM_ARCHIVO', null=True),
        ),
    ]