import time
import threading
from django.http import HttpResponse
from django.db import transaction
from .models import Item

# Q1 + Q2
def test_signal(request):
    start = time.time()

    print(f"View Thread ID: {threading.get_ident()}")

    Item.objects.create(name="Test Item")

    end = time.time()

    return HttpResponse(f"Time taken: {end - start} seconds")


# Q3: Transaction test
def test_transaction(request):
    try:
        with transaction.atomic():
            Item.objects.create(name="Rollback Item")
            print("Item created inside transaction")

            raise Exception("Force rollback")

    except:
        pass

    exists = Item.objects.filter(name="Rollback Item").exists()

    return HttpResponse(f"Exists after rollback? {exists}")