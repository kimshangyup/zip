# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buddy', '0003_auto_20150528_1937'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetail',
            name='username',
        ),
        migrations.DeleteModel(
            name='UserDetail',
        ),
    ]
