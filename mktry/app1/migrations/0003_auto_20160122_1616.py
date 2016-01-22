# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20160122_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='try_carousel',
            name='createdate',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 22, 8, 16, 11, 516000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='try_carousel',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 22, 8, 16, 11, 516000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='try_carousel',
            name='state',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='try_carousel',
            name='type',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
