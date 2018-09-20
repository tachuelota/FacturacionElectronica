# Generated by Django 2.0.6 on 2018-08-31 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0008_cliente'),
    ]

    operations = [
        migrations.AddField(
            model_name='comprobantecab',
            name='cffecven',
            field=models.DateTimeField(blank=True, db_column='CFFECVEN', null=True),
        ),
        migrations.AddField(
            model_name='comprobantecab',
            name='sumatoria_descuentos',
            field=models.DecimalField(blank=True, db_column='SUMATORIA_DESCUENTOS', decimal_places=2, max_digits=12, null=True),
        ),
    ]