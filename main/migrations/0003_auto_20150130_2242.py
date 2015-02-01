# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20150130_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musicsample',
            name='text',
            field=models.CharField(max_length=2000),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='writingsample',
            name='text',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
