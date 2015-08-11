# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('framgia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contact_name', models.CharField(max_length=500, verbose_name=b'Name')),
                ('contact_email', models.CharField(max_length=500, verbose_name=b'Email')),
                ('contact_telephone', models.CharField(max_length=15, verbose_name=b'Telephone')),
                ('contact_message', models.CharField(max_length=5000, verbose_name=b'Message')),
            ],
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
