# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookstores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddressStore',
            fields=[
                ('store_ptr', models.OneToOneField(serialize=False, auto_created=True, parent_link=True, primary_key=True, to='bookstores.Store')),
                ('x_coordinate', models.CharField(max_length=20)),
                ('y_coordinate', models.CharField(max_length=20)),
            ],
            bases=('bookstores.store',),
        ),
    ]
