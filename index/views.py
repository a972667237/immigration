#coding: utf-8
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def index(requests):
    article = Article.objects.all()
    return render(requests, 'index.html', locals())


def expert(requests):
    return render(requests, 'expert.html')

def about(requests):
    return render(requests, 'about.html')

def culturl(requests):
    article = Article.objects.all()
    return render(requests, 'culture.html', locals())

def contact(requests):
    return render(requests, 'contact.html')


def article(requests):
    article_id = requests.GET.get('id', 1)
    try:
        article_id = int(article_id)
    except:
        article_id = 1
    if article_id == 4:
        return render(requests, 'australia_knowledge.html', locals())
    if article_id == 5:
        return render(requests, 'newzeland_knowledge.html', locals())
    if article_id == 6:
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
        if not email:
            return HttpResponse("必须输入邮箱")
        comment = requests.POST.get('comment')
        try:
            Info(name=name, phone=phone, email=email, comment=comment).save()
        except:
            return HttpResponse("不可预知的错误")
        return HttpResponse("提交成功")
    return HttpResponse("访问错误")