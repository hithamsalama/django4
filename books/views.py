from http.client import ImproperConnectionState
from operator import imod
from pkgutil import ImpImporter
import re
from django.shortcuts import render
from .models import Book, Borrower 
from . import forms
from .forms  import NewBook_form
from django.core import validators
from django.contrib.auth.decorators import login_required

# Create your views here.

def landing(request):
    mydect2 = {'name2':'This is a landing page !!  '}
    return render(request, "landing_page.html",context=mydect2)


def books(request):
    books_view = Book.objects.order_by('id')
    books_dict= {'book_key': books_view}
    return render(request, "books/books_page.html",context=books_dict)

#def form_name_view(request):
#    form = forms.Register_a_book()
#    return render(request, "books/register_a_book.html",context={'form':form})


def form_name_view(request):
    form = forms.NewBook_form()
    if request.method == "POST":
        form = NewBook_form(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return books(request)
        else:
            
            print(form.errors)

    return render(request, "books/register_a_book.html",context={'form':form})
