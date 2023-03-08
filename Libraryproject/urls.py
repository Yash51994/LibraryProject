"""Libraryproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from lib_app.views import homepage, show_books, edit_book,delete_book, show_published_books, restore_book
from lib_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', homepage, name='home'),
    path('show-books/', show_books, name='show_books'),
    path('edit-book/<int:pk>/', edit_book, name='edit_book'),
    path('delete-book/<int:pk>/', delete_book, name='delete_book'),
    path('published-books/', show_published_books, name='published_books'),
    path('restore-book/<int:pk>/', restore_book, name='restore_book'),

    path('form-view/', views.form_view, name='form_view'),
    path('update-view/<int:pk>/', views.update_view, name='update_view'),

    path('cbv-home/', views.Home.as_view(), name='cbv_home'),
    
    path('gen-tempview/', views.about_us.as_view(), name='gen_tempview'),
    path('gen-redirectview/', views.TestRedirect.as_view(), name='redirectview'),




]
