from django import forms
from django.db import models
from django.forms import fields, widgets
from . models import Book
CHOICES_SORT = (
    ("1", "Name_asc"),
    ("2", "Name_desc"),
    ("3", "Count_asc"),
    ("4", "Count_desc"),
)

CHOICES_FILTER = (
    ("1", "Author_id="),
    ("2", "Count="),
    ("3", "Name_contains"),
    ("4", "Desc_contains"),
)


class QueryForm(forms.Form):
    author_id = forms.IntegerField(label='author_id')


class UserForm(forms.Form):
    user_id = forms.IntegerField(label='user_id')


class BookIDForm(forms.Form):
    book_id = forms.IntegerField(label='book_id')


class UserLoginForm(forms.Form):
    username = forms.CharField(label='username')
    password = forms.CharField(label='password')


class SortFilterForm(forms.Form):
    sort = forms.ChoiceField(choices=CHOICES_SORT, required=False)
    filter = forms.ChoiceField(choices=CHOICES_FILTER, required=False)
    find = forms.CharField(max_length=100, required=False)


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('name', 'description', 'count')

        widgets={
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Book name'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Small description'}),
            'count': forms.TextInput(attrs={'class':'form-control'}),
            # 'authors': forms.Select(attrs={'class':'form-control'})
        }


class BookFormUpdate(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('name', 'description', 'count')

        widgets={
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Book name'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Small description'}),
            'count': forms.TextInput(attrs={'class':'form-control'}),
            'authors': forms.Select(attrs={'class':'form-control'})
        }


class OrderForm(forms.Form):
    day = forms.ChoiceField(choices= [(x, x) for x in range(1, 20)])