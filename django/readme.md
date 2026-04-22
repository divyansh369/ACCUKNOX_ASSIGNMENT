# Django Signals Assignment

## Objective
Demonstrate the behavior of Django signals with respect to:
1. Synchronous vs Asynchronous execution
2. Thread execution context
3. Database transaction behavior

---


Question 1: By default are django signals executed synchronously or asynchronously? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

Answer: Django signals are executed synchronously by default. This is proven by introducing a delay (time.sleep(3)) inside the signal handler. The HTTP response is delayed until the signal execution completes, confirming blocking behavior.

Question 2: Do django signals run in the same thread as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

Answer: Django signals run in the same thread as the caller. This is verified by printing thread IDs using threading.get_ident() in both the view and signal handler. The IDs match, proving same-thread execution.

Question 3: By default do django signals run in the same database transaction as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

Answer: Django signals run within the same database transaction as the caller. This is demonstrated using transaction.atomic(). Even though the signal executes, the database changes are rolled back, confirming that signals execute before transaction commit.