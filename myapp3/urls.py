from django.urls import path
from .views import week_orders, month_orders, year_orders, product_form

urlpatterns = [
    path('week/', week_orders, name='week_orders'),
    path('month/', month_orders, name='month_orders'),
    path('year/', year_orders, name='year_orders'),
    path('product/add/', product_form, name='product_form'),

]
