#coding: utf-8
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

COVER_MAP = {
    "article": ["australia_top.jpg", "newzeland.jpg", "canada_culture.jpg", "australia_guide_top.jpg", "newzeland_top.jpg", "canada.jpg", "culture_more.jpeg", "culture_more.jpeg", "culture_more.jpeg", "australia.jpg", "newzeland.jpg", "canada.jpg"],
    "expert": "people.jpeg",
    "culture": "culture_more.jpeg",
    "contact": "contact_more.jpg",
    "about": "about.jpg"
}

def index(requests):
    article = Article.objects.all()
    spiderInfo = Spider_info.objects.all()[0]
    video = Video.objects.get(pk=1)
    return render(requests, 'index.html', locals())


def expert(requests):
    spiderInfo = Spider_info.objects.all()[0]
    img = COVER_MAP.get("expert")
    return render(requests, 'expert.html', locals())

def about(requests):
    spiderInfo = Spider_info.objects.all()[0]
    img = COVER_MAP.get("about")
    art = Article.objects.get(pk=13)
    return render(requests, 'about.html', locals())

def culturl(requests):
    spiderInfo = Spider_info.objects.all()[0]
    img = COVER_MAP.get("culture")
    article = Article.objects.all()
    return render(requests, 'culture.html', locals())

def contact(requests):
    spiderInfo = Spider_info.objects.all()[0]
    img = COVER_MAP.get("contact")
    art = Article.objects.get(pk=14)
    return render(requests, 'contact.html', locals())


def article(requests):
    spiderInfo = Spider_info.objects.all()[0]
    article_id = requests.GET.get('id', 1)
    try:
        article_id = int(article_id)
    except:
        article_id = 1
    img = COVER_MAP.get("article")[article_id-1]
    if article_id == 4:
        res = Knowledge.objects.filter(country = 1)
        return render(requests, 'australia_knowledge.html', locals())
    if article_id == 5:
        res = Knowledge.objects.filter(country = 2)
        return render(requests, 'newzeland_knowledge.html', locals())
    if article_id == 6:
        res = Knowledge.objects.filter(country = 3)
        return render(requests, 'canada_knowledge.html', locals())

    art = Article.objects.get(pk=article_id)
    return render(requests, 'article.html', locals())

def info_submit(requests):
    if requests.method == "POST":
        import re
        name = requests.POST.get('name')
        if len(name) == 0:
            return HttpResponse("必须输入名字")
        phone = requests.POST.get('phone')
        p = re.compile('^0\d{2,3}\d{7,8}$|^1[3578]\d{9}$|^147\d{8}')
        if not p.match(phone):
            return HttpResponse("手机格式有误")
        email = requests.POST.get('email')
        comment = requests.POST.get('comment')
        try:
            Info(name=name, phone=phone, email=email, comment=comment).save()
        except:
            return HttpResponse("不可预知的错误")
        return HttpResponse("提交成功")
    return HttpResponse("访问错误")
