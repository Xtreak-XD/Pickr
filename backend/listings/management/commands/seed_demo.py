from django.core.management.base import BaseCommand
from listings.models import Product, Listing, Source

class Command(BaseCommand):
    help = "Seeds demo products/listings"

    def handle(self, *args, **kwargs):
        product, _ = Product.objects.get_or_create(
            title="Apple AirPods Pro",
            brand="Apple",
            category="electronics",
            asin="B09JQK9DK5",
        )
        Listing.objects.get_or_create(
            product=product,
            source=Source.AMAZON,
            external_id="B09JQK9DK5",
            defaults=dict(price=199.00, currency="USD",
                          url="https://example.com/airpods", condition="New"),
        )
        self.stdout.write(self.style.SUCCESS("Seeded demo listing"))