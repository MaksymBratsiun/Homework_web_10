from django.contrib import admin
from django.urls import path

from . import views

app_name = 'app_quotes'

urlpatterns = [
    path('', views.main, name='root'),
    path('page/', views.page, name='page'),
    path('author/<int:author_id>', views.author, name='author'),
    path('create_author/', views.create_author, name='create_author'),
    path('create_quote/', views.create_quote, name='create_quote'),
    path('tag/', views.tag, name='tag'),
]
