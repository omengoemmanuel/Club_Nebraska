from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages


# Create your views here.

def index(request):
    categories = MenuCategory.objects.all()
    menu_items = MenuItem.objects.all()
    specials = Special.objects.all()
    event = Event.objects.all()
    testi = testimonials.objects.all()
    gal = gallery.objects.all()
    staf = staff.objects.all()
    return render(request, 'index.html',
                  {'categories': categories, 'menu_items': menu_items, 'specials': specials, 'event': event,
                   'testi': testi, 'gal': gal, 'staf':staf})


def book_table(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        time = request.POST.get('time')
        no_of_people = request.POST.get('no_of_people')
        message = request.POST.get('message')

        bk_table = table(name=name, email=email, phone=phone, date=date, time=time, no_of_people=no_of_people,
                         message=message)
        bk_table.save()
        messages.success(request, 'Table booking details send. Kindly wait for confirming email for the approval')
        return redirect('index')
    return redirect('index')


def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        cont = contact(name=name, email=email, subject=subject, message=message)
        cont.save()
        messages.success(request,"Message sent successfully")
        return redirect('index')
    return redirect('index')