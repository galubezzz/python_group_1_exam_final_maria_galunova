from django.contrib import admin
from webapp.models import Author, Book

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'date_of_birth', 'date_of_death']


class BookAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'year']

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
