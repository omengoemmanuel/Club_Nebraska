from django.shortcuts import render

# Create your views here.

def admin_board(request):
    return render(request, 'dashboard1/index.html')