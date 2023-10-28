from django.contrib import admin
from .models import User, Product, Order


@admin.action(description="Заказ выполнен")
def order_completed(modeladmin, request, queryset):
    queryset.update(is_completed=True)


@admin.action(description="Все по 10$")
def sale_10(modeladmin, request, queryset):
    queryset.update(price=10)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'amount']
    ordering = ['amount']
    search_fields = ['name']
    search_help_text = 'Поиск по названию продукта'
    actions = [sale_10]
    fields = ['name', 'description', 'price', 'amount', 'addition_date']
    readonly_fields = ['addition_date']


class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'addres']
    list_filter = ['addres']
    search_fields = ['name']
    search_help_text = 'Поиск по имени пользователя'
    readonly_fields = ['registration_date']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Личные данные',
            {
                'classes': ['collapse'],
                'description': 'Личные данные пользователя',
                'fields': ['email', 'phone_number', 'addres'],
            },
        ),
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['registration_date'],
            },
        ),
    ]


class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'total_price',
                    'date_ordered', 'is_completed']
    ordering = ['is_completed', 'date_ordered']
    list_filter = ['is_completed', 'total_price']
    actions = [order_completed]
    fields = ['customer', 'total_price', 'date_ordered', 'is_completed']
    readonly_fields = ['date_ordered']


admin.site.register(User, UserAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
