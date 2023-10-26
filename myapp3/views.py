from django.views import View
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from myapp3.models import Order, Product, Product_new
import datetime
from datetime import date
from .forms import ProductForm
from django.core.files.storage import FileSystemStorage


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


def product_form(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            amount = form.cleaned_data['amount']
            addition_date = form.cleaned_data['addition_date']
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            image_format = image.name.split('.')[1]
            image_name = name+'.'+image_format
            fs.save(image_name, image)
            product = Product_new(name=name, description=description,
                                  price=price, amount=amount, addition_date=addition_date)
            product.save()
            message = 'Товар добавлен'
    else:
        form = ProductForm()
        message = 'Заполните форму'
    return render(request, 'myapp3/product_form.html', {'form':
                                                        form})
