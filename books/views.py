from http.client import ImproperConnectionState
from operator import imod
from pkgutil import ImpImporter
import re
from django.shortcuts import render
from .models import Book, Borrower 
from . import forms
from . import models
from .forms  import NewBook_form
from django.core import validators
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.views.generic import View,TemplateView,ListView,DetailView,FormView
# Create your views here.


def landing(request):
    mydect2 = {'name2':'This is a landing page !!  '}
    return render(request, "landing_page.html",context=mydect2)

class IndexView(TemplateView):
    template_name = "landing_page.html"


class BooksListView(ListView):
    paginate_by = 5
    model = Book
#    template_name = 'books/bookslist.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
#        context['book'] = Book.objects.all()
        return context

class BooksDetailView(DetailView):
    context_object_name='book_detail'
    model = Book
    template_name = 'books/book_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['boook'] = Book.objects.all()
        return context

def books(request):
    
    books_view = Book.objects.all()
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
