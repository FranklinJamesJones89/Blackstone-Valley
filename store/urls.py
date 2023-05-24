from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('', views.index, name='index'),
    path('dispensary-menu', views.dispensary_menu, name='dispensary-menu'),
    path('about', views.about, name='about'),
    path('category/<str:pk>/', views.category, name='category')
]
