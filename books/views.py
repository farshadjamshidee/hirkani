from django.shortcuts import render, redirect
from django.http import HttpResponse
from books.models import Book
from django.template import loader
from .forms import BookForm

# Create your views here.
def index(request):
    all_book = Book.objects.all()
    template = loader.get_template('books/index.html')
    context = {
        'all_book':all_book
    }
    return HttpResponse(template.render(context, request))


def add_book(request):
    context= {}
    form =  BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    context['form'] = form

    return render(request, 'books/add_book.html', context)

