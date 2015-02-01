# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20150130_2242'),
    ]

    operations = [
        migrations.AddField(
            model_name='writingsample',
            name='writing_type',
            field=models.CharField(default=b'', max_length=100),
            preserve_default=True,
        ),
    ]
