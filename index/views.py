from django.shortcuts import render
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
    return render(requests, 'culture.html')

def contact(requests):
    return render(requests, 'contact.html')


def article(requests):
    article_id = requests.GET.get('id')
    art = Article.objects.get(pk=article_id)
    return render(requests, 'article.html', locals())