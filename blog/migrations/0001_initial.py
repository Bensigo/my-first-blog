# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('author', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=150)),
                ('text', models.TextField()),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('time_publish', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
