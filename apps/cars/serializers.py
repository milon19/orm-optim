from rest_framework import serializers
from django.db.models import Avg

from apps.cars.models import (
    Car,
    Company,
    RentalPackage,
    RentalAddon,
    RentalAddonLocalPrice,
    Currency,
    CarLocalPrice,
    CarPrice,
)


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = [
            'id',
            'name',
        ]


class RentalAddonSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField()
    currency = serializers.SerializerMethodField()

    def get_price(self, obj):
        currency_id = self.context.get('request').query_params.get('currency')
        price  = RentalAddonLocalPrice.objects.filter(
            addon=obj, currency_id=currency_id
        ).first()
        return price.local_price if price else 0

    def get_currency(self, obj):
        currency_id = self.context.get('request').query_params.get('currency')
        currency = Currency.objects.filter(id=currency_id).first()
        return {
            'id': currency.id,
            'code': currency.code,
            'name': currency.name,
        }

    class Meta:
        model = RentalAddon
        fields = [
            'id',
            'name',
            'price',
            'currency',
            'pricing_unit',
        ]


class RentalPackageSerializer(serializers.ModelSerializer):
    addons = RentalAddonSerializer(many=True)
    total_addon_price = serializers.SerializerMethodField()

    def get_total_addon_price(self, obj):
        currency_id = self.context.get('request').query_params.get('currency')
        total_addon_price = 0
        for addon in obj.addons.all():
            price = RentalAddonLocalPrice.objects.filter(
                addon=addon, currency_id=currency_id
            ).first()
            total_addon_price += price.local_price if price else 0
        return total_addon_price

    class Meta:
        model = RentalPackage
        fields = [
            "id",
            "name",
            "is_default",
            "addons",
            "total_addon_price",
        ]

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = "__all__"

class CarLocalPriceSerializer(serializers.ModelSerializer):
    currency = CurrencySerializer()

    class Meta:
        model = CarLocalPrice
        fields = "__all__"


class CarPriceSerializer(serializers.ModelSerializer):
    local_price = CarLocalPriceSerializer(source='car_local_prices', many=True)
    base_currency = CurrencySerializer()

    class Meta:
        model = CarPrice
        fields = "__all__"


class CarListSerializer(serializers.ModelSerializer):
    from_location = serializers.CharField(source='from_location.name')
    to_location = serializers.SerializerMethodField()
    from_date = serializers.SerializerMethodField()
    to_date = serializers.SerializerMethodField()
    company = CompanySerializer()
    # packages = RentalPackageSerializer(many=True, source='car_rental_packages')
    prices = CarPriceSerializer(many=True, source='car_prices')

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
            "id",
            "name",
            "from_location",
            "to_location",
            "from_date",
            "to_date",
            "company",
            # "packages",
            "prices",
        ]