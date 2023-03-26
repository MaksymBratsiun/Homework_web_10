from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import AuthorForm, TagForm, QuoteForm
from .models import Author, Quote, Tag


# Create your views here.


def main(request):
    return render(request, 'app_quotes/index.html', context={'title': 'Quotes'})


def page(request):
    return render(request, 'app_quotes/page.html', context={'title': 'Quotes'})


def author(request):
    return render(request, 'app_quotes/author.html', context={'title': 'Quotes'})


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
            res = form.save(commit=False)
            res.user = request.user
            res.save()
            return redirect(to='app_quotes:root')
    return render(request, 'app_quotes/create_author.html', context={'title': 'Quotes', 'form': form})


@login_required
def create_quote(request):
    tags = Tag.objects.all()  # noqa
    authors = Author.objects.all()  # noqa
    if request.method == 'POST':
        form = QuoteForm(request.POST, instance=Quote())
        if form.is_valid():
            new_quote = form.save(commit=False)
            choice_tags = Tag.objects.filter(name__in=request.POST.getlist('tags')) # noqa
            choice_authors = Author.objects.filter(name__in=request.POST.getlist('authors'))  # noqa
            for tag_ in choice_tags.iterator():
                new_quote.tags.add(tag_)
            for author_ in choice_authors.iterator():
                new_quote.tags.add(author_)
            new_quote.user = request.user
            new_quote.save()
            return redirect(to='app_quotes:root')
        else:
            return render(request, 'app_quotes/create_quote.html', {'tags': tags, 'authors': authors, 'form': form})
    return render(request, 'app_quotes/create_quote.html', {'tags': tags, 'authors': authors, 'form': QuoteForm()})
