from django.conf import settings
from django.db import models

class SwipeType(models.TextChoices):
    LIKE = "LIKE", "Like"
    PASS = "PASS", "Pass"
    SUPERLIKE = "SUPERLIKE", "Superlike"

class Swipe(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="swipes")
    listing = models.ForeignKey("listings.Listing", on_delete=models.CASCADE, related_name="swipes")
    action = models.CharField(max_length=10, choices=SwipeType.choices)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = [("user", "listing")]
        indexes = [
            models.Index(fields=["user", "created_at"]),
            models.Index(fields=["listing", "created_at"]),
        ]

class Match(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="matches")
    listing = models.ForeignKey("listings.Listing", on_delete=models.CASCADE, related_name="matches")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = [("user", "listing")]
        indexes = [models.Index(fields=["user", "created_at"])]
        indexes = [models.Index(fields=["user", "created_at"])]
