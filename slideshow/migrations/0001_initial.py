# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import slideshow.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SlideHome',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('titulo', models.CharField(max_length=20, verbose_name=b'T\xc3\xadtulo')),
                ('foto', models.ImageField(upload_to=slideshow.models.upload_to_foto)),
            ],
            options={
                'verbose_name_plural': 'Home',
            },
            bases=(models.Model,),
        ),
    ]
