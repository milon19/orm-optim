from django.http import HttpResponse
from django.urls import path

from apps.core import views

app_name = "core"

urlpatterns = [
    path(
        "health-check/",
        lambda request: HttpResponse(status=200),
        name="health-check",
    ),
    path(
        "hello-world/",
        views.HelloWorldAPIView.as_view(),
    )
]
