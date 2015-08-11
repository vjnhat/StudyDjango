# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('blog_title', models.CharField(max_length=500, verbose_name=b'Title')),
                ('blog_summary', models.CharField(max_length=10000, verbose_name=b'Summary')),
                ('blog_images', models.CharField(max_length=500, verbose_name=b'Image')),
                ('blog_date', models.DateTimeField(verbose_name=b'Date')),
                ('blog_content', models.CharField(max_length=20000, verbose_name=b'Content')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category_name', models.CharField(max_length=500, verbose_name=b'Category Name')),
                ('category_description', models.CharField(max_length=10000, verbose_name=b'Description')),
            ],
        ),
    ]
