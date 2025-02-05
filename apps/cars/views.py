from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView

from apps.cars.models import Car
from apps.cars.serializers import CarListSerializer


class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class CarListAPIView(APIView):
    serializer_class = CarListSerializer
    pagination_class = CustomPageNumberPagination


    def get_queryset(self):
        qs = Car.objects.all()
        return qs

    def get(self, request):
        qs = self.get_queryset()
        paginator = self.pagination_class()
        paginated_queryset = paginator.paginate_queryset(qs, request)
        serializer = self.serializer_class(paginated_queryset, many=True)
        return paginator.get_paginated_response(serializer.data)
