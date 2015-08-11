__author__ = 'FRAMGIA\le.cong.phuc'
from django.db import models


class Contact(models.Model):
    contact_name=models.CharField('Name', max_length=500)
    contact_email=models.CharField('Email', max_length=500)
    contact_telephone=models.CharField('Telephone', max_length=15)
    contact_message=models.CharField('Message',max_length=5000)

    class Meta:
        app_label='framgia'
