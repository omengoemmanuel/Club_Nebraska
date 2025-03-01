from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('book_table', views.book_table, name='book_table'),
    path('contacts', views.contacts, name='contacts'),

]