# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tsdb', '0002_auto_20141230_0305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='lyrics',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='song',
            name='title',
            field=models.CharField(max_length=80),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='song',
            name='video_url',
            field=models.CharField(max_length=80),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='songtranslation',
            name='lyrics',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='songtranslation',
            name='title',
            field=models.CharField(max_length=80),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='songtranslation',
            name='video_url',
            field=models.CharField(max_length=80),
            preserve_default=True,
        ),
    ]
