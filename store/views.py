from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'store/index.html')

def dispensary_menu(request):
    return render(request, 'store/dispensary-menu.html')

def about(request):
    return render(request, 'store/about.html')
