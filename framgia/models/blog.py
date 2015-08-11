__author__ = 'FRAMGIA\le.cong.phuc'
from django.db import models


class Blog(models.Model):
    blog_title=models.CharField('Title', max_length=500)
    blog_summary=models.CharField('Summary', max_length=10000)
    blog_images=models.CharField('Image',max_length=500)
    blog_date=models.DateTimeField('Date')
    blog_content=models.CharField('Content',max_length=20000)

    class Meta:
        app_label='framgia'
