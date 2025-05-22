from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView

from apps.cars.filters import CarListFilter
from apps.cars.models import Car
from apps.cars.serializers import CarListSerializer


class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class CarListAPIView(APIView):
    serializer_class = CarListSerializer
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = CarListFilter


    def get_queryset(self):
        queryset = Car.objects.all().select_related("company").prefetch_related(
            "car_rental_packages",
            "car_rental_packages__addons",
            "car_rental_packages__addons__currency",
            "car_prices",
            "car_prices__base_currency",
        )
        for backend in self.filter_backends:
            queryset = backend().filter_queryset(self.request, queryset, self)
        return queryset

    def get(self, request):
        qs = self.get_queryset()
        paginator = self.pagination_class()
        paginated_queryset = paginator.paginate_queryset(qs, request)
        serializer = self.serializer_class(
            paginated_queryset, many=True, context={"request": request}
        )
        return paginator.get_paginated_response(serializer.data)
