from django.contrib import admin
from .models import Product, Listing

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "brand", "category", "asin", "created_at")
    search_fields = ("title", "brand", "asin", "upc", "gtin")
    list_filter = ("brand", "category")

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ("product", "source", "external_id", "price", "is_active", "last_seen_at")
    search_fields = ("external_id", "product__title")
    list_filter = ("source", "is_active")
