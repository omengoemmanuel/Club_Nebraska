from django.shortcuts import render

# Create your views here.

def admin_board(request):
    return render(request, 'dashboard1/dashboard.html')

def layout(request):
    return render(request, 'dashboard1/layout.html')