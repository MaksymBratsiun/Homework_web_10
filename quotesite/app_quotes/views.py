from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import AuthorForm
from .models import Author, Quote
# Create your views here.


def main(request):
    return render(request, 'app_quotes/index.html', context={'title': 'Quotes'})


def page(request):
    return render(request, 'app_quotes/page.html', context={'title': 'Quotes'})


def author(request):
    return render(request, 'app_quotes/author.html', context={'title': 'Quotes'})


@login_required
def create_author(request):
    form = AuthorForm(instance=Author())
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=Author())
        if form.is_valid():
            res = form.save(commit=False)
            res.user = request.user
            res.save()
            return redirect(to='app_quotes:root')
    return render(request, 'app_quotes/create_author.html', context={'title': 'Quotes', 'form': form})


@login_required
def create_quote(request):
    return render(request, 'app_quotes/create_author', context={'title': 'Quotes'})


def search(request):
    return render(request, 'app_quotes/search.html', context={'title': 'Quotes'})
