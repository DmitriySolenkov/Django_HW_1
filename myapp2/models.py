from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.PositiveIntegerField()
    addres = models.TextField()
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}, {self.email}, {self.phone_number}, {self.addres}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default='', blank=True)
    price = models.DecimalField(
        default=999999.99, max_digits=8, decimal_places=2)
    amount = models.PositiveSmallIntegerField(default=0)
    addition_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}, {self.description}, {self.price}, {self.amount}'


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(
        default=999999.99, max_digits=8, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.customer.name}, {self.total_price}, {self.date_ordered}, {self.is_completed}'
