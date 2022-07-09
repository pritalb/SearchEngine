from django import views
from django.urls import path
from  . import views

urlpatterns = [
    path('search/q=<str:query>', views.search, name='search')
]
