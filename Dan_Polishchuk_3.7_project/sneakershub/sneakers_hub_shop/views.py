from sqlite3 import connect
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import *

def index(request):
    products = Product.objects.all()
    return render(request, 'sneakers_hub_shop/index.html', {'products': products})

def order(request, **kwargs):
    if request.method == 'POST':
        model = request.GET.get('model')
        price = request.GET.get('price')
        size = request.POST.get('shoe size')
        fname = request.POST.get('first name')
        lname = request.POST.get('last name')
        email = request.POST.get('email')
        address = request.POST.get('address')

        Orders.objects.create(Model=model, Price=price, Size=size, First_Name=fname, Last_Name=lname, Email=email, Address=address)
 
        return HttpResponseRedirect(reverse('thanks'))
    else:
        model = request.GET.get('model')
        price = request.GET.get('price')
        return render(request, 'sneakers_hub_shop/order_form.html', {'model': model, 'price': price})

def thank_you(request):
    return render(request, 'sneakers_hub_shop/thanks.html')
