from django.shortcuts import render
import datetime

from product.models import Category

def index(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'store/index.html', context)

def dispensary_menu(request):
    current_time = datetime.datetime.now().time()
    
    if current_time < datetime.time(20,0) and current_time >= datetime.time(10,0):
        business = 'Open'
    else:
        business = 'Closed'

    categories = Category.objects.all()

    context = {'categories': categories, 'business': business}

    return render(request, 'store/dispensary-menu.html', context)

def about(request):
    return render(request, 'store/about.html')
