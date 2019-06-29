from django import forms
from django.contrib.auth.models import User
from webapp.models import Author, Book, Review


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        date_of_birth = forms.DateField(widget=forms.SelectDateWidget())
        date_of_death = forms.DateField(widget=forms.SelectDateWidget())
        fields = ['name', 'date_of_birth', 'date_of_death', 'image', 'biography']


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'year', 'image', 'file', 'description']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text']
