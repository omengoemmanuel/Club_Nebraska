from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


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
    return render(request, 'dashboard1/dashboard.html')


def layout(request):
    return render(request, 'dashboard1/layout.html')


@login_required
def profile(request):
    return render(request, 'dashboard1/profile.html')


@login_required()
def settings(request):
    return render(request, 'dashboard1/settings.html')
