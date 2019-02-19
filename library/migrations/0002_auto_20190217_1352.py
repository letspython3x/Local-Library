# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='Scholar_name',
        ),
        migrations.AddField(
            model_name='post',
            name='ISBN',
            field=models.IntegerField(default=4546378982176),
        ),
        migrations.AddField(
            model_name='post',
            name='genre',
            field=models.CharField(default='educational', max_length=30),
            preserve_default=False,
        ),
    ]
