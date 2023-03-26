from django.forms import ModelForm, TextInput, CharField, Textarea
from .models import Author, Quote


class AuthorForm(ModelForm):
    fullname = CharField(max_length=150, widget=TextInput(attrs={'class': 'form-control'}))
    born_date = CharField(max_length=200, widget=TextInput(attrs={'class': 'form-control'}))
    born_location = CharField(max_length=200, widget=TextInput(attrs={'class': 'form-control'}))
    description = CharField(max_length=5000,
                            widget=Textarea(attrs={'class': 'form-control', 'rows': '8', 'placeholder': 'Input here'}))

    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']
