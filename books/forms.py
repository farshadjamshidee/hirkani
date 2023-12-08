from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields =[
            'caption','brief', 'author', 'count', 'cost'
        ]