from random import choices, randint, random
from django.core.management.base import BaseCommand
from myapp3.models import User, Product, Order
import datetime
import random

LOREM = "Lorem ipsum dolor sit amet, consectetur adipisicing elit Accusamus accusantium aut beatae consequatur consequuntur cumque, delectus et illo iste maxime nihil non nostrum odio officia perferendis placeat quasi quibusdam quisquam quod sunt tempore temporibus ut voluptatum aliquam culpa ducimus eaque eum illo mollitia nemo tempore unde vero! Blanditiis deleniti ex hic"


class Command(BaseCommand):
    help = "Generate 20 orders and 30 products for 1 user"

    def handle(self, *args, **options):
        text = LOREM.split()
        user = User(name='John', email='mail@mail.com',
                    phone_number=911, addres='Minsk')
        user.save()

        products = []

        for i in range(1, 31):
            product = Product(name=(" ".join(choices(
                text, k=1)).capitalize()), description='description', price=round(random.uniform(1.00, 100.00), 2), amount=randint(5, 15))
            products.append(product)
            product.save()

        for j in range(1, 21):
            month = randint(7, 10)
            if month == 10:
                day = randint(1, 25)
            else:
                day = randint(1, 30)
            date = datetime.date(2023, month, day)
            order = Order(customer=user, total_price=round(
                random.uniform(20.00, 150.00), 2), date_ordered=date)
            order.save()
            for g in range(3):
                order.products.add(products[randint(1, 25)])
            order.save()
