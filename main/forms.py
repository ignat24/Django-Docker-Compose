from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db.models import fields
from django.forms import widgets
from authentication.models import CustomUser
from django.contrib.auth import password_validation
from django.utils.translation import gettext as _


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=12, min_length=4, required=True,
                                 widget=forms.TextInput(
                                     attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    middle_name = forms.CharField(max_length=12, required=False,
                                widget=(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Middle Name'})))
    last_name = forms.CharField(max_length=12, min_length=4, required=True,
                                widget=(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'})))
    email = forms.EmailField(max_length=50,
                             widget=(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'})))
    password1 = forms.CharField(label=_('Password'),
                                widget=(forms.PasswordInput(attrs={'class': 'form-control'})))
                                # help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(label=_('Password Confirmation'),
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = CustomUser
        fields = ('first_name', 'middle_name', 'last_name', 'email', 'password1', 'password2',)



class LoginForm(forms.Form):
    # class Meta:
    #     model = CustomUser
    #     fields = ('email', 'password')

    #     widgets = {
    #         'email': forms.TextInput(attrs={'class':'form-control', 'placeholder':'email'}),
    #         'password': forms.TextInput(attrs={'class':'form-control', 'placeholder':'password'}),
    #     }
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class CustomUserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=12, min_length=4, required=True,
                                 widget=forms.TextInput(
                                     attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    middle_name = forms.CharField(max_length=12, required=False,
                                widget=(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Middle Name'})))
    last_name = forms.CharField(max_length=12, min_length=4, required=True,
                                widget=(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'})))
    email = forms.EmailField(max_length=50,
                             widget=(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'})))
    password1 = forms.CharField(label=_('Password'),
                                widget=(forms.PasswordInput(attrs={'class': 'form-control'})),
                                help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(label=_('Password Confirmation'),
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = CustomUser
        fields = ('first_name', 'middle_name', 'last_name', 'email', 'password1', 'password2',)
