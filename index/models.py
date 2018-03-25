#coding: utf-8
from __future__ import unicode_literals

from django.db import models
from DjangoUeditor.models import UEditorField
from util import upload_video_cover

class Article(models.Model):
    title = models.CharField(u'标题', max_length=100)
    description = models.TextField(u'简介', max_length=1000)
    content = UEditorField(u'内容', max_length=200000)
    date = models.DateField(u'创建时间', auto_now_add=True, editable=True)
    cover = models.ImageField(u'封面图片', upload_to=upload_video_cover, default="/static/imgs/canada.jpg")
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

class Video(models.Model):
    video = models.FileField(u'上传视频，要求mp4格式', upload_to=upload_video_cover)
    description = models.CharField(u'视频描述', max_length=1000)
    class Meta:
        verbose_name = '视频'
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return "首页视频"

class Spider_info(models.Model):
    keywords = models.CharField(u'关键词（英文逗号分隔，别超过四个关键词）', max_length=1000)
    description = models.TextField(u'描述', max_length=1000)
    class Meta:
        verbose_name = '推广信息'
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return u'推广信息'