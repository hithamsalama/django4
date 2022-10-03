from urllib.parse import urlparse
from django.urls import path
from . import views

app_name= 'books'
urlpatterns = [
    path('', views.landing,name='landing'),
    path('books/', views.books,name='view_books'),
    path('books/register/',views.form_name_view,name="add_a_book")
]