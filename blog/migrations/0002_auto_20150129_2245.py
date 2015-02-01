# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='post_title',
            field=models.CharField(default=b'', max_length=500),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blogcomments',
            name='comment_title',
            field=models.CharField(default=b'', max_length=500),
            preserve_default=True,
        ),
    ]
