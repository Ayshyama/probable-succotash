from django.contrib import admin
from django.urls import include
from django.urls import path
from django.utils.translation import gettext_lazy as _

urlpatterns = [
    path('admin/', admin.site.urls),
    path(_('orders/'), include('orders.urls')),
]
