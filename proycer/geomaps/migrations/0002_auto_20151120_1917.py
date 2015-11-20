# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('geomaps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cosude',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cosude', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='ueducativa',
            name='coordenadas',
            field=geoposition.fields.GeopositionField(default=b'-16.687980, -68.286467', max_length=42),
        ),
        migrations.AddField(
            model_name='ueducativa',
            name='cosude',
            field=models.ForeignKey(default=0, to='geomaps.Cosude'),
        ),
    ]
