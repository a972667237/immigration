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