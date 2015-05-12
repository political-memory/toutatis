# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('export_data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exportedrevision',
            name='dossier_reference',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
