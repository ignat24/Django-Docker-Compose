from django import forms
from . models import Author
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('name', 'surname', 'patronymic')

        widgets={
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Author name'}),
            'surname': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Author surname'}),
            'patronymic': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Author patronymic'}),
        }