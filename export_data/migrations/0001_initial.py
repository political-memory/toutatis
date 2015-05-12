# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExportedRevision',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data', models.TextField()),
                ('checksum', models.CharField(unique=True, max_length=255)),
                ('creation_datetime', models.DateTimeField()),
                ('last_check_datetime', models.DateTimeField()),
            ],
            options={
                'ordering': ['-last_check_datetime'],
            },
            bases=(models.Model,),
        ),
    ]
