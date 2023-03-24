from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.


def main(request):
    return render(request, 'app_quotes/index.html', context={'title': 'Quotes'})


def page(request):
    return render(request, 'app_quotes/page.html', context={'title': 'Quotes'})


def author(request):
    return render(request, 'app_quotes/author.html', context={'title': 'Quotes'})


@login_required
def create_author(request):
    return render(request, 'app_quotes/index.html', context={'title': 'Quotes'})


@login_required
def create_quote(request):
    return render(request, 'app_quotes/index.html', context={'title': 'Quotes'})


def search(request):
    return render(request, 'app_quotes/search.html', context={'title': 'Quotes'})
