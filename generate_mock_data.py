from django.core.management.base import BaseCommand
from chatbot.models import Product
import random

class Command(BaseCommand):
    help = 'Generates mock data for products'

    def handle(self, *args, **kwargs):
        categories = ['Laptop', 'Smartphone', 'Tablet', 'Camera', 'Headphones']
        for i in range(1, 101):
            Product.objects.create(
                name=f'Product {i}',
                description=f'Description for product {i}',
                price=round(random.uniform(100.0, 1000.0), 2),
                category=random.choice(categories)
            )
        self.stdout.write(self.style.SUCCESS('Successfully generated 100 mock products'))
