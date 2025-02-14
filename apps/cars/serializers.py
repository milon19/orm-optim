from rest_framework import serializers

from apps.cars.models import Car, Company, RentalPackage


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = [
            'id',
            'name',
        ]

class RentalPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentalPackage
        fields = [
            'id',
            'name',
            "is_default"
        ]


class CarListSerializer(serializers.ModelSerializer):
    from_location = serializers.CharField(source='from_location.name')
    to_location = serializers.SerializerMethodField()
    from_date = serializers.SerializerMethodField()
    to_date = serializers.SerializerMethodField()
    company = CompanySerializer()
    packages = RentalPackageSerializer(many=True, source='car_rental_packages')

    def get_from_date(self, obj):
        from_date = self.context.get('request').query_params.get('from_date')
        return from_date

    def get_to_date(self, obj):
        to_date = self.context.get('request').query_params.get('to_date')
        return to_date

    def get_to_location(self, obj):
        return obj.to_location.name

    class Meta:
        model = Car
        fields = [
            'id',
            'name',
            'from_location',
            "to_location",
            "from_date",
            "to_date",
            "company",
            "packages",
        ]