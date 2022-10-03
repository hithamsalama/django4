from urllib.parse import urlparse
from django.urls import path
from . import views

app_name= 'library_users'
urlpatterns = [
    path('library_users/', views.the_index,name='index'),
    path('library_users/register', views.register,name='register'),
    path('library_users/login',view=views.user_login, name='login'),
    path('library_users/logout',view=views.user_logout, name='logout')

]