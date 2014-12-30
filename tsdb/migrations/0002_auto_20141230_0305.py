# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tsdb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='songtranslation',
            old_name='song',
            new_name='orig',
        ),
        migrations.AddField(
            model_name='song',
            name='video_url',
            field=models.CharField(max_length=120, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='songtranslation',
            name='lang',
            field=models.CharField(max_length=3, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='songtranslation',
            name='title',
            field=models.CharField(max_length=200, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='songtranslation',
            name='video_url',
            field=models.CharField(max_length=120, default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='song',
            name='artist',
            field=models.ForeignKey(to='tsdb.Artist'),
            preserve_default=True,
        ),
    ]
