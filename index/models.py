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


class Info(models.Model):
    name = models.CharField(u'名字', max_length=100)
    phone = models.CharField(u'电话', max_length=11)
    email = models.EmailField(u'邮箱', max_length=200, null=True)
    comment = models.TextField(u"评论", max_length=50000)
    isRead = models.BooleanField(u"是否已读", default=False)
    create_date = models.DateField(u"创建时间", auto_now_add=True, editable=False)

    class Meta:
        verbose_name = '用户提交信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name + "/" + self.create_date.strftime('%Y-%m-%d') + "/" + (u"已读" if self.isRead else u"未读")