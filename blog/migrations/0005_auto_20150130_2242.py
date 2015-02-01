# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20150129_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomment',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 30, 22, 42, 25, 895956, tzinfo=utc), verbose_name=b'date published'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blogcomment',
            name='text',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 30, 22, 42, 25, 895465, tzinfo=utc), verbose_name=b'date published'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='text',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
