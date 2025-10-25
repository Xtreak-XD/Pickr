from django.db import models

class Source(models.TextChoices):
    AMAZON = "AMAZON", "Amazon"
    FBM = "FB_MARKETPLACE", "Facebook Marketplace"
    EBAY = "EBAY", "eBay"
    OTHER = "OTHER", "Other"

class Product(models.Model):
    title = models.CharField(max_length=300, db_index=True)
    brand = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=120, blank=True)
    description = models.TextField(blank=True)
    asin = models.CharField(max_length=20, blank=True, db_index=True)
    upc = models.CharField(max_length=24, blank=True, db_index=True)
    gtin = models.CharField(max_length=24, blank=True, db_index=True)
    dedupe_key = models.CharField(max_length=64, blank=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=["title"]),
            models.Index(fields=["brand", "category"]),
        ]

    def __str__(self):
        return self.title

class Listing(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="listings")
    source = models.CharField(max_length=20, choices=Source.choices, db_index=True)
    external_id = models.CharField(max_length=64, db_index=True)
    url = models.URLField(max_length=1000, blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    currency = models.CharField(max_length=8, default="USD")
    condition = models.CharField(max_length=64, blank=True)
    location_text = models.CharField(max_length=160, blank=True)
    thumbnail_url = models.URLField(max_length=1000, blank=True)
    is_active = models.BooleanField(default=True)
    last_seen_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = [("source", "external_id")]
        indexes = [
            models.Index(fields=["source", "external_id"]),
            models.Index(fields=["price"]),
            models.Index(fields=["is_active", "last_seen_at"]),
        ]

    def __str__(self):
        return f"{self.source}:{self.external_id}"
