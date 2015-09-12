# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import base.models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('request_stamp', models.DateTimeField(auto_now_add=True)),
                ('served_stamp', models.DateTimeField(default=base.models.now_plus_thirty)),
                ('message', models.TextField(max_length=5000)),
                ('court', models.ForeignKey(to='base.Court')),
            ],
        ),
    ]
