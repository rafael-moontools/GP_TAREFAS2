# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('profile_photo', models.CharField(max_length=255, null=True, verbose_name='Profile Picture', blank=True)),
                ('cover_photo', models.CharField(max_length=255, null=True, blank=True)),
                ('display_name', models.CharField(max_length=150, null=True, blank=True)),
                ('language', models.CharField(max_length=6, null=True, blank=True)),
                ('gender', models.CharField(max_length=1, verbose_name='G\xeanero', choices=[(b'M', 'Masculino'), (b'F', 'Feminino')])),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
