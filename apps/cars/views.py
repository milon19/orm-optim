from rest_framework.views import APIView

from rest_framework.response import Response

from apps.cars.models import Car
from apps.cars.serializers import CarListSerializer


class CarListAPIView(APIView):
    serializer_class = CarListSerializer

    def get_queryset(self):
        return Car.objects.all()

    def get(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)