import json
import uuid
from decimal import Decimal
from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.utils.dateparse import parse_datetime
from .models import Listing, Product

def _serialize_listing(l: Listing) -> dict:
    return {
        "id": l.id,
        "product_id": l.product_id,
        "source": l.source,
        "external_id": l.external_id,
        "url": l.url,
        "price": float(l.price) if l.price is not None else None,
        "currency": l.currency,
        "condition": l.condition,
        "location_text": l.location_text,
        "thumbnail_url": l.thumbnail_url,
        "is_active": l.is_active,
        "last_seen_at": l.last_seen_at.isoformat() if l.last_seen_at else None,
        "created_at": l.created_at.isoformat() if l.created_at else None,
    }

@csrf_exempt
def listings_collection(request):
    if request.method == "GET":
        limit = int(request.GET.get("limit", 20))
        offset = int(request.GET.get("offset", 0))
        qs = Listing.objects.filter(is_active=True).order_by("-created_at")[offset:offset+limit]
        return JsonResponse([_serialize_listing(x) for x in qs], safe=False)

    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))
        except Exception:
            return HttpResponseBadRequest("Invalid JSON")
        # minimal required fields: product_id, source, external_id
        try:
            product = Product.objects.get(id=data["product_id"])
        except (KeyError, Product.DoesNotExist):
            return HttpResponseBadRequest("Missing or invalid product_id")

        listing = Listing.objects.create(
            product=product,
            source=data.get("source", "OTHER"),
            external_id=data.get("external_id", str(uuid.uuid4())),
            url=data.get("url", ""),
            price=Decimal(str(data["price"])) if "price" in data and data["price"] is not None else None,
            currency=data.get("currency", "USD"),
            condition=data.get("condition", ""),
            location_text=data.get("location_text", ""),
            thumbnail_url=data.get("thumbnail_url", ""),
            is_active=bool(data.get("is_active", True)),
        )
        return JsonResponse(_serialize_listing(listing), status=201)

    return HttpResponseNotAllowed(["GET", "POST"])

@csrf_exempt
def listings_item(request, listing_id):
    try:
        obj = Listing.objects.get(id=listing_id)
    except Listing.DoesNotExist:
        return JsonResponse({"detail": "Not found"}, status=404)

    if request.method == "GET":
        return JsonResponse(_serialize_listing(obj))

    if request.method == "PATCH":
        try:
            data = json.loads(request.body.decode("utf-8"))
        except Exception:
            return HttpResponseBadRequest("Invalid JSON")

        for field in ["url", "currency", "condition", "location_text", "thumbnail_url"]:
            if field in data:
                setattr(obj, field, data[field])
        if "price" in data:
            obj.price = Decimal(str(data["price"])) if data["price"] is not None else None
        if "is_active" in data:
            obj.is_active = bool(data["is_active"])
        obj.save()
        return JsonResponse(_serialize_listing(obj))

    if request.method == "DELETE":
        obj.delete()
        return JsonResponse({"ok": True})

    return HttpResponseNotAllowed(["GET", "PATCH", "DELETE"])
