# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('price', models.CharField(max_length=12)),
                ('startdate', models.CharField(max_length=10)),
                ('enddate', models.CharField(max_length=10)),
                ('kind', models.CharField(max_length=30)),
                ('option', models.CharField(max_length=20)),
                ('etc', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
