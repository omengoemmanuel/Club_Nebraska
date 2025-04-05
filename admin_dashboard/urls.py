from django.urls import path
from . import views

urlpatterns = [
    path('/', views.admin_login, name='admin_login'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('admin_board/', views.admin_board, name='admin_board'),
    path('layout/', views.layout, name='layout'),
    path('profile/', views.profile, name='profile'),
    path('settings/', views.settings, name='settings'),
    path('staffs/', views.staffs, name='staffs'),
    path('add_staff/', views.add_staff, name='add_staff'),

]
