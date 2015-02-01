# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_writingsample_writing_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='musicsample',
            name='static_audio_location',
        ),
        migrations.AddField(
            model_name='musicsample',
            name='embed_html',
            field=models.CharField(default=b'', max_length=600),
            preserve_default=True,
        ),
    ]
