# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20150130_1156'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(default=b'M', max_length=1, verbose_name='G\xeanero', choices=[(b'M', 'Masculino'), (b'F', 'Feminino')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='language',
            field=models.CharField(max_length=6, null=True, blank=True),
            preserve_default=True,
        ),
    ]
