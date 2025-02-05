from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView

from rest_framework.response import Response

from apps.cars.models import Car
from apps.cars.serializers import CarListSerializer


class CarListAPIView(APIView):
    serializer_class = CarListSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        return Car.objects.all()

    def get(self, request):
        qs = self.get_queryset()
        paginator = self.pagination_class()
        paginated_queryset = paginator.paginate_queryset(qs, request, self)
        serializer = self.serializer_class(paginated_queryset, many=True)
        return paginator.get_paginated_response(serializer.data)
