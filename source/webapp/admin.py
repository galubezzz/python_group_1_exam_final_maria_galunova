from django.contrib import admin
from webapp.models import Author

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'date_of_birth', 'date_of_death']



admin.site.register(Author, AuthorAdmin)

