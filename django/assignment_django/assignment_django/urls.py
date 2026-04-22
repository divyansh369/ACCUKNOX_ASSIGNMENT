# myproject/urls.py

from django.contrib import admin
from django.urls import path
from myapp.views import test_signal, test_transaction

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', test_signal),
    path('transaction/', test_transaction),
]