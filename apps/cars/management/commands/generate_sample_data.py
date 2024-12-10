from django.core.management.base import BaseCommand
from apps.cars.factories import (
    CompanyFactory,
    LocationFactory,
    CurrencyFactory,
    CarFactory,
    CarPriceFactory,
    CarLocalPriceFactory,
    RentalAddonFactory,
    RentalPackageFactory,
    RentalAddonLocalPriceFactory
)


class Command(BaseCommand):
    help = "Generate sample data for car rental models using Factory Boy"

    def handle(self, *args, **kwargs):

        CurrencyFactory.create_batch(4)
        LocationFactory.create_batch(4)
        CompanyFactory.create_batch(2)
        CarFactory.create_batch(5)
        CarPriceFactory.create_batch(10)
        CarLocalPriceFactory.create_batch(10)
        RentalAddonFactory.create_batch(3)
        RentalPackageFactory.create_batch(5)
        RentalAddonLocalPriceFactory.create_batch(6)

        self.stdout.write(self.style.SUCCESS(
            "Sample data has been generated successfully using Factory Boy!"
        ))
