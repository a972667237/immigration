from django.shortcuts import render

# Create your views here.
def index(requests):
    return render(requests, 'index.html')


def expert(requests):
    return render(requests, 'expert.html')

def about(requests):
    return render(requests, 'about.html')

def culturl(requests):
    return render(requests, 'culture.html')

def contact(requests):
    return render(requests, 'contact.html')