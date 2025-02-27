from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from debug_toolbar.toolbar import debug_toolbar_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("apps.core.urls")),
    path("", include("apps.cars.urls")),
] + debug_toolbar_urls()
