from data_processor.models import carParts, clothesItems, techItems, toys, forYouPage
from django.db import IntegrityError
from django.forms.models import model_to_dict
from django.core.exceptions import SynchronousOnlyOperation
from concurrent.futures import ThreadPoolExecutor


def add_item(ModelClass, item_data: dict) -> tuple:
    try:
        item = ModelClass.objects.create(**item_data)
        return (item, None)
    except SynchronousOnlyOperation as e:
        # ORM was called from an async event loop in this thread. Run the synchronous
        # create in a separate thread to avoid SynchronousOnlyOperation.
        try:
            def _create():
                return ModelClass.objects.create(**item_data)

            with ThreadPoolExecutor(max_workers=1) as ex:
                future = ex.submit(_create)
                item = future.result()
            return (item, None)
        except Exception as e2:
            return (None, str(e2))
    except IntegrityError as e:
        return (None, str(e))
    except Exception as e:
        return (None, str(e))

def update_item(ModeClass, title_to_find: str, new_data: dict) -> tuple:
    try:
        update_count = ModeClass.objects.filter(title__iexact=title_to_find).update(**new_data)
        if update_count > 0:
            return True
        else:
            return False
    except Exception as e:
        return False

def delete_item(ModelClass, title_to_find: str) -> tuple:
    try:
        delete_count, _ = ModelClass.objects.filter(title__iexact=title_to_find).delete()
        if delete_count > 0:
            return True
        else:
            return False
    except Exception as e:
        return False

def get_item_by_title(ModelClass, title_to_find:str):
    try:
        return ModelClass.objects.get(title__iexact=title_to_find)
    except ModelClass.DoesNotExist:
        return None
