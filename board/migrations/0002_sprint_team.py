# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sprint',
            name='team',
            field=models.ForeignKey(default=1, to='board.Team'),
            preserve_default=False,
        ),
    ]
