# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buddy', '0002_auto_20150511_0146'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetail',
            name='language',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userdetail',
            name='nationality',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
