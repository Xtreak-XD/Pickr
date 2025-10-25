from django.contrib import admin
from .models import Swipe, Match

@admin.register(Swipe)
class SwipeAdmin(admin.ModelAdmin):
    list_display = ("user", "listing", "action", "created_at")
    list_filter = ("action",)
    search_fields = ("user__username", "listing__external_id")

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ("user", "listing", "created_at")
    search_fields = ("user__username", "listing__external_id")
