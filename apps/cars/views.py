from django.db.models import Prefetch, Subquery, OuterRef
from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView

from apps.cars.filters import CarListFilter
from apps.cars.models import (
    Car,
    RentalPackage,
    RentalAddonLocalPrice,
    RentalAddon,
    CarPrice,
    CarLocalPrice,
)
from apps.cars.serializers import CarListSerializer


class CustomPageNumberPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 100


class CarListAPIView(APIView):
    serializer_class = CarListSerializer
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = CarListFilter
    # renderer_classes = [JSONRenderer]

    def get_queryset(self):
        from_date = self.request.query_params.get('from_date')
        to_date = self.request.query_params.get('to_date')
        currency_id = self.request.query_params.get('currency')
        car_local_prices_qs = CarLocalPrice.objects.filter(currency_id=currency_id).select_related('currency')
        car_prices_qs = CarPrice.objects.filter(from_date__lte=to_date, to_date__gte=from_date).prefetch_related(
            Prefetch('car_local_prices', queryset=car_local_prices_qs)
        ).select_related('base_currency')
        queryset = Car.objects.select_related(
            'company', 'from_location', 'to_location'
        ).prefetch_related(
            Prefetch('car_prices', queryset=car_prices_qs)
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
