from rest_framework import serializers

from apps.cars.models import Car


class CarListSerializer(serializers.ModelSerializer):
    from_location = serializers.CharField(source='from_location.name')
    to_location = serializers.SerializerMethodField()

    def get_to_location(self, obj):
        return obj.to_location.name

    class Meta:
        model = Car
        fields = [
            'id',
            'name',
            'from_location',
            "to_location",
        ]