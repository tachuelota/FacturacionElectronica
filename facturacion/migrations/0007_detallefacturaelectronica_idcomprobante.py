# Generated by Django 2.0.6 on 2018-06-18 00:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0006_auto_20180617_1914'),
    ]

    operations = [
        migrations.AddField(
            model_name='detallefacturaelectronica',
            name='idComprobante',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='facturacion.FacturaElectronica'),
        ),
    ]