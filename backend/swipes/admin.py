from django.contrib import admin
from .models import Swipe, Match

@admin.register(Swipe)
class SwipeAdmin(admin.ModelAdmin):
    list_display = ("user", "product", "action", "created_at")
    list_filter = ("action",)
    search_fields = ("user__username", "product__name")

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ("user", "product", "created_at")
    search_fields = ("user__username", "product__name")
