from django.forms import ModelForm, TextInput, CharField, Textarea, ModelChoiceField, ChoiceField
from .models import Author, Quote, Tag


class AuthorForm(ModelForm):
    fullname = CharField(max_length=150, widget=TextInput(attrs={'class': 'form-control'}))
    born_date = CharField(max_length=200, widget=TextInput(attrs={'class': 'form-control'}))
    born_location = CharField(max_length=200, widget=TextInput(attrs={'class': 'form-control'}))
    description = CharField(max_length=5000,
                            widget=Textarea(attrs={'class': 'form-control', 'rows': '8', 'placeholder': 'Input here'}))

    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']


class TagForm(ModelForm):
    name = CharField(min_length=3, max_length=25, required=True, widget=TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Tag
        fields = ['name']


class QuoteForm(ModelForm):
    quote = CharField(max_length=1500,
                      required=True,
                      widget=Textarea(attrs={'class': 'form-control', 'rows': '3', 'placeholder': 'Input here'}))
    author = ModelChoiceField(queryset=Author.objects.all(), required=True) # noqa

    class Meta:
        model = Quote
        fields = ['quote', 'author']
        exclude = ['tags']

