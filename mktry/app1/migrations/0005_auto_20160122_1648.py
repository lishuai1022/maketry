# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_auto_20160122_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='try_carousel',
            name='createdate',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 22, 8, 48, 40, 703000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='try_carousel',
            name='img_url',
            field=models.FileField(upload_to=b'./app1/static/app1/'),
        ),
        migrations.AlterField(
            model_name='try_carousel',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 22, 8, 48, 40, 703000, tzinfo=utc)),
        ),
    ]
