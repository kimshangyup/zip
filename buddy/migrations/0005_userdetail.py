# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('buddy', '0004_auto_20150531_1710'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=30)),
                ('age', models.CharField(max_length=5)),
                ('address', models.CharField(max_length=30)),
                ('channel', models.CharField(max_length=10)),
                ('introduce', models.CharField(max_length=200)),
                ('nationality', models.CharField(max_length=20)),
                ('language', models.CharField(max_length=20)),
                ('occupation', models.CharField(max_length=20)),
                ('preference', models.CharField(max_length=30)),
                ('kakao', models.CharField(max_length=15)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
    ]
