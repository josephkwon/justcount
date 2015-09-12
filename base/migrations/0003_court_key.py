# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_ticket'),
    ]

    operations = [
        migrations.AddField(
            model_name='court',
            name='key',
            field=models.CharField(default='This Is The Default Password 123$%^', max_length=100),
        ),
    ]
