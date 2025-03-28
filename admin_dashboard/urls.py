from django.urls import path
from .import views

urlpatterns = [
    path('admin', views.admin_board, name='admin_board'),
    path('layout', views.layout, name='layout'),
]