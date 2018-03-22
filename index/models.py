#coding: utf-8
from __future__ import unicode_literals

from django.db import models
from DjangoUeditor.models import UEditorField

# Create your models here.

class Article(models.Model):
    title = models.CharField(u'标题', max_length=100)
    description = models.TextField(u'简介', max_length=1000)
    content = UEditorField(u'内容', max_length=200000)
    date = models.DateField(u'创建时间', auto_now_add=True, editable=True)
    class Meta:
        verbose_name = u'文章'
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return self.title