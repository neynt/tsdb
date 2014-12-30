# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('artist', models.CharField(max_length=80)),
                ('lyrics', models.CharField(max_length=10000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SongTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('translator', models.CharField(max_length=80)),
                ('lyrics', models.CharField(max_length=10000)),
                ('song', models.ForeignKey(to='tsdb.Song')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
