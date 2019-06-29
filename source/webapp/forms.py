from django import forms
from django.contrib.auth.models import User
from webapp.models import Author


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'date_of_birth', 'date_of_death', 'image', 'biography']
