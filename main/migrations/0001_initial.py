# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MusicSample',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=500)),
                ('text', models.CharField(max_length=5000)),
                ('static_audio_location', models.CharField(default=None, max_length=500, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WritingSample',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=500)),
                ('text', models.CharField(max_length=10000)),
                ('static_img_location', models.CharField(default=None, max_length=500, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
