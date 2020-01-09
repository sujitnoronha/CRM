from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def home(request):
    orders = Order.objects.all()
    customers = Customers.objects.all()
    total_customers = Customers.objects.count()
    total_orders = orders.count()

    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()


    context = {
        'orders':orders,
        'customers': customers,
        'total_orders':total_orders,
        'delivered': delivered,
        'pending': pending
    }

    return render(request, 'accounts/dashboard.html',context)

def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {'products': products})

def customer(request, pk):
    customer = Customers.objects.get(id = pk)
    orders = customer.order_set.all()
    orders_count = orders.filter(id = pk).count 
    context = {
        'customer':customer,'orders':orders,'order_count': orders_count
    }

    return render(request, 'accounts/customer.html',context)