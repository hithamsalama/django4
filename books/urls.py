from urllib.parse import urlparse
from django.urls import path,re_path
from . import views
from .views import BooksListView,BooksDetailView
app_name= 'books'
urlpatterns = [
    path('', views.landing,name='landing'),
    path('books', views.books,name='view_books'),
    path('bookslist/', BooksListView.as_view(),name='view_books_list'),
    path('books/register/',views.form_name_view,name="add_a_book"),
#    path('bookslist/<slug:slug>/',BooksDetailView.as_view(),name='book_detail'),
#    re_path(r'^(?P<slug>[-\w]+)/$', BooksDetailView.as_view(),name='book_detail'),
    re_path(r'^bookslist/(?P<pk>[-\w]+)$', views.BooksDetailView.as_view(),name='book_detail')
]