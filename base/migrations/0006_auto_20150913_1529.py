# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_auto_20150913_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='name',
            field=models.CharField(max_length=40),
        ),
    ]
