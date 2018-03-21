from django.shortcuts import render

# Create your views here.
def index(requests):
    return render(requests, 'index.html')


def expert(requests):
    return render(requests, 'expert.html')