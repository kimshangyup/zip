# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buddy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetail',
            name='occupation',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='age',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='channel',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='introduce',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='kakao',
            field=models.CharField(max_length=15),
        ),
    ]
