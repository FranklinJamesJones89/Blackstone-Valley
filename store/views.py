from django.shortcuts import render
import datetime

from product.models import Category, Product

def index(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'store/index.html', context)

def dispensary_menu(request):
    categories = Category.objects.all()
    product = Product.objects.all()
    
    current_time = datetime.datetime.now().time()
    
    if current_time < datetime.time(20,0) and current_time >= datetime.time(10,0):
        business = 'Open'
    else:
        business = 'Closed'

    context = {'categories': categories, 'business': business, 'product': product}

    return render(request, 'store/dispensary-menu.html', context)

def about(request):
    return render(request, 'store/about.html')

def category(request, pk):
    category = Category.objects.get(id=pk)
    product = category.product_set.order_by('-created_at')

    context = {'category': category, 'product': product}

    return render(request, 'store/category.html', context)
