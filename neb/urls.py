from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('book_table', views.book_table, name='book_table'),
    path('contacts', views.contacts, name='contacts'),
    path('menu_view', views.menu_view, name='menu_view'),
    path('generate_qr_code', views.generate_qr_code, name='generate_qr_code'),

]