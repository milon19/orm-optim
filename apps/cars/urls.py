from django.urls import path

from apps.cars import views

app_name = "cars"

urlpatterns = [
    path(
        "cars/",
        views.CarListAPIView.as_view(),
        name="cars-list",
    ),
]
