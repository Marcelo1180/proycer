# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('geomaps', '0002_auto_20151120_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ueducativa',
            name='coordenadas',
            field=geoposition.fields.GeopositionField(max_length=42),
        ),
        migrations.AlterField(
            model_name='ueducativa',
            name='cosude',
            field=models.ForeignKey(to='geomaps.Cosude'),
        ),
    ]
