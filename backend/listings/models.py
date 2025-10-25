from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    tags = models.JSONField(default=list, blank=True)  # List of tags
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField(default=0.0)  # 0.0 to 5.0
    store = models.CharField(max_length=100)

    def __str__(self):
        return self.name
