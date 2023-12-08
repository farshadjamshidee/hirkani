from django.contrib import admin
from books.models import Author, Book
# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name','last_name']


class BookAdmin(admin.ModelAdmin):
    list_display = ['caption','author','count']

admin.site.register(Author,AuthorAdmin)
admin.site.register(Book, BookAdmin)