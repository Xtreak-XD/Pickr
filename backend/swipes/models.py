from django.conf import settings
from django.db import models

class SwipeType(models.TextChoices):
    LIKE = "LIKE", "Like"
    PASS = "PASS", "Pass"
    SUPERLIKE = "SUPERLIKE", "Superlike"

class Swipe(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="swipes")
    product = models.ForeignKey("listings.Product", on_delete=models.CASCADE, related_name="swipes")
    action = models.CharField(max_length=10, choices=SwipeType.choices)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = [("user", "product")]
        indexes = [
            models.Index(fields=["user", "created_at"]),
            models.Index(fields=["product", "created_at"]),
        ]

class Match(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="matches")
    product = models.ForeignKey("listings.Product", on_delete=models.CASCADE, related_name="matches")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = [("user", "product")]
        indexes = [models.Index(fields=["user", "created_at"])]
