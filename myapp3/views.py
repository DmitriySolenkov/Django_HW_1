from django.views import View
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from myapp3.models import Order, Product
import datetime
from datetime import date


def my_view(request):
    context = {"name": "John"}
    return render(request, "myapp3/index.html", context)


def week_orders(request):
    date_now = date.today()
    products = []
    for i in range(1, 21):
        order = get_object_or_404(Order, pk=i)
        if date_now-order.date_ordered <= datetime.timedelta(days=7):
            for product in order.products.all().values_list():
                if product[1] not in products:
                    products.append(product[1])
    context = {"period": "прошедшую неделю", "products": products}
    return render(request, "myapp3/time_sort.html", context)


def month_orders(request):
    date_now = date.today()
    products = []
    for i in range(1, 21):
        order = get_object_or_404(Order, pk=i)
        if date_now-order.date_ordered <= datetime.timedelta(days=30):
            for product in order.products.all().values_list():
                if product[1] not in products:
                    products.append(product[1])
    context = {"period": "прошедший месяц", "products": products}
    return render(request, "myapp3/time_sort.html", context)

def year_orders(request):
    date_now = date.today()
    products = []
    for i in range(1, 21):
        order = get_object_or_404(Order, pk=i)
        if date_now-order.date_ordered <= datetime.timedelta(days=365):
            for product in order.products.all().values_list():
                if product[1] not in products:
                    products.append(product[1])
    context = {"period": "прошедший год", "products": products}
    return render(request, "myapp3/time_sort.html", context)
