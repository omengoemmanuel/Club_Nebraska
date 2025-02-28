from tkinter import Menu

from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(MenuCategory)
admin.site.register(MenuItem)
admin.site.register(Special)