# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_ticket_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='request_stamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
