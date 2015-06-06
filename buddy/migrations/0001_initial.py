# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=30)),
                ('age', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('channel', models.CharField(max_length=30)),
                ('introduce', models.CharField(max_length=30)),
                ('preference', models.CharField(max_length=30)),
                ('kakao', models.CharField(max_length=30)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('username', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
