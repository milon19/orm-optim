from rest_framework.serializers import ModelSerializer

from apps.cars.models import Car


class CarListSerializer(ModelSerializer):
    class Meta:
        model = Car
        fields = [
            'id',
            'name',
            'from_location',
            "to_location",
        ]