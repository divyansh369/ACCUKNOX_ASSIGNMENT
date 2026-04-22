import time
import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Item

@receiver(post_save, sender=Item)
def my_signal(sender, instance, **kwargs):
    print("\n--- SIGNAL START ---")

    # Q1: Sync proof (delay)
    print("Sleeping for 3 seconds...")
    time.sleep(3)

    # Q2: Thread proof
    print(f"Signal Thread ID: {threading.get_ident()}")

    print("--- SIGNAL END ---\n")