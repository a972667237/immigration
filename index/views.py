from django.shortcuts import render

# Create your views here.
def index(requests):
    return render(requests, 'index.html')


def base(requests):
    return render(requests, 'base.html')