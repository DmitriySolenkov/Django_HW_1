from django.core.management.base import BaseCommand
from myapp2.models import User


class Command(BaseCommand):
    help = "Create user."

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='User name')
        parser.add_argument('email', type=str, help='User email')
        parser.add_argument('phone_number', type=int, help='User phone_number')
        parser.add_argument('addres', type=str, help='User addres')

    def handle(self, *args, **kwargs):
        user_name = kwargs.get('name')
        user_email = kwargs.get('email')
        user_phone_number = kwargs.get('phone_number')
        user_addres = kwargs.get('addres')
        user = User(name=user_name, email=user_email,
                    phone_number=user_phone_number, addres=user_addres)
        user.save()
        self.stdout.write(f'{user}')
