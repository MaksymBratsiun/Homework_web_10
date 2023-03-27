from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import AuthorForm, TagForm, QuoteForm
from .models import Author, Quote, Tag


# Create your views here.


def main(request):
    quotes_ = Quote.objects.all()[:10]
    return render(request, 'app_quotes/index.html', context={'title': 'Quotes', 'quotes': quotes_})


def page(request):
    return render(request, 'app_quotes/page.html', context={'title': 'Quotes'})


def author(request, author_id):
    author_ = get_object_or_404(Author, pk=author_id)
    return render(request, 'app_quotes/author.html', {"author": author_})


def tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST, instance=Tag())
        if form.is_valid():
            form.save()
            return redirect(to='app_quotes:root')
        else:
            return render(request, 'app_quotes/tag.html', {'form': form})
    return render(request, 'app_quotes/tag.html', {'form': TagForm()})


@login_required
def create_author(request):
    form = AuthorForm(instance=Author())
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=Author())
        if form.is_valid():
            form.save()
            return redirect(to='app_quotes:root')
    return render(request, 'app_quotes/create_author.html', context={'title': 'Quotes', 'form': form})


@login_required
def create_quote(request):
    form = QuoteForm()
    if request.method == "POST":
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='app_quotes:root')
        else:
            return render(request, 'app_quotes/create_quote.html', {'form': form})
    return render(request, 'app_quotes/create_quote.html', {'form': form})


