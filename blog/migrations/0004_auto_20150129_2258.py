# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150129_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomment',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 29, 22, 58, 32, 898182, tzinfo=utc), verbose_name=b'date published'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 29, 22, 58, 32, 897698, tzinfo=utc), verbose_name=b'date published'),
            preserve_default=True,
        ),
    ]
