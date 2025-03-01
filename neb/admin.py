from tkinter import Menu

from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(MenuCategory)
admin.site.register(MenuItem)
admin.site.register(Special)
admin.site.register(Event)
admin.site.register(table)
admin.site.register(testimonials)
admin.site.register(gallery)
admin.site.register(contact)
admin.site.register(staff)

