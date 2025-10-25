from django.urls import path
from . import views

urlpatterns = [
    path("", views.listings_collection),            # GET=list, POST=create
    path("<int:listing_id>/", views.listings_item)  # GET, PATCH, DELETE
]