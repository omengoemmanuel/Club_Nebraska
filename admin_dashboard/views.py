from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from neb.models import *

from django.http import JsonResponse
from django.shortcuts import get_object_or_404



# Create your views here.

# Login view
def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_staff:
                login(request, user)
                return redirect('admin_board')
            else:
                messages.error(request, "You are not authorized to access this page.")
                return redirect('admin_login')
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'dashboard1/login.html')


def logout_user(request):
    logout(request)
    return redirect('admin_login')


@login_required
def admin_board(request):
    t_book = table.objects.count()
    s_message = contact.objects.count()
    testi = testimonials.objects.all()
    return render(request, 'dashboard1/dashboard.html', {'t_book': t_book, 's_message': s_message, 'testi': testi})


def layout(request):
    return render(request, 'dashboard1/layout.html')


@login_required
def profile(request):
    return render(request, 'dashboard1/profile.html')


@login_required()
def settings(request):
    return render(request, 'dashboard1/settings.html')


@login_required()
def staffs(request):
    staf = staff.objects.all()
    return render(request, 'dashboard1/staff.html', {'staf': staf})

# add staff
def add_staff(request):
    if request.method == 'POST':
        name = request.POST['name']
        position = request.POST['position']
        X_link = request.POST.get('X_link')
        facebook = request.POST.get('facebook')
        instagram = request.POST.get('instagram')
        linkedin = request.POST.get('linkedin')
        image = request.FILES['image']

        ad_staff = staff(name=name, position=position, X_link=X_link, facebook=facebook, instagram=instagram, linkedin=linkedin, image=image)
        ad_staff.save()
        messages.success(request, "Staff added successfully.")
        return redirect('staffs')
    return redirect('staffs')

# table booking
@login_required()
def table_booking(request):
    tab_book= table.objects.all()
    return render(request, 'dashboard1/tablebooking.html', {'tab_book': tab_book})

# loading bookings inside a modal
def get_table_booking(request, id):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        booktable = get_object_or_404(table, id=id)
        data = {
            "name": table.name,
            "email": table.email,
            "phone": table.phone,
            "date": table.date.strftime("%d/%m/%Y"),
            "time": table.time.strftime("%H:%M"),
            "no_of_people": table.no_of_people,
            "message": table.message,
            "status": table.status,
            "approving_staff": table.approving_staff,
        }
        return JsonResponse(data)
    return JsonResponse({'error': 'Invalid request'}, status=400)