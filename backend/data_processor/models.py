from django.db import models

#model for all General Items
class Productbase(models.Model):
    title = models.CharField(max_length=100, verbose_name="product Title", null=True, blank=True)
    price = models.CharField(max_length=100, null=True, blank=True)
    ratings = models.CharField(max_length=100, null=True, blank=True)
    subCategory = models.CharField(max_length=150, null=True, blank=True)
    mainCategory = models.CharField(max_length=150, null=True, blank=True)
    img_link = models.CharField(max_length=300, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    #extra for you pg
    userOpinion = models.DecimalField(max_digits=3, decimal_places=1, default=3.0)

    class Meta:
        abstract = True #makes an abstract class

class techItems(Productbase):
    tech_field = models.CharField(max_length=120, default='Tech')

class carParts(Productbase):
    carParts_field = models.CharField(max_length=120, default='CarParts')

class toys(Productbase):
    toys_field = models.CharField(max_length=120, default='Toys')

class clothesItems(Productbase):
    clothes_field = models.CharField(max_length=120, default='Clothes')

class forYouPage(Productbase):
    forYou_field = models.CharField(max_length=120, default='FYP')

