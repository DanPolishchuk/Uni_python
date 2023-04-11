from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('order_form/', order, name='order_form'),
    path('thanks/', thank_you, name='thanks'),
]