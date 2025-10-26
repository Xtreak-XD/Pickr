from django.urls import path
from .views import get_automotives, get_clothes, get_FYP, get_techItems, get_toys

urlpatterns = [
    path('categories/autos', get_automotives, name='get_automotives'),
    path('categories/toys', get_toys, name='et_toys'),
    path('categories/tech', get_techItems, name='get_techItems'),
    path('categories/fyp', get_FYP, name='get_FYP'),
    path('categories/clothes', get_clothes, name='get_clothes'),
]