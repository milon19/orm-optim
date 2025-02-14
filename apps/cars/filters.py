from django_filters import rest_framework as filters

from apps.cars.models import Car


class CarListFilter(filters.FilterSet):
    from_date = filters.DateFilter(
        field_name='car_prices__from_date', lookup_expr='gte',
    )
    to_date = filters.DateFilter(
        field_name='car_prices__to_date', lookup_expr='lte'
    )
    from_location = filters.CharFilter(
        field_name='from_location__name', lookup_expr='icontains'
    )
    to_location = filters.CharFilter(
        field_name='to_location__name', lookup_expr='icontains'
    )

    class Meta:
        model = Car
        fields = ['from_date', 'to_date', 'from_location', 'to_location']