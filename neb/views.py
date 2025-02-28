from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    categories = MenuCategory.objects.all()
    menu_items = MenuItem.objects.all()
    specials = Special.objects.all()
    return render(request, 'index.html', {'categories': categories, 'menu_items': menu_items, 'specials': specials})


