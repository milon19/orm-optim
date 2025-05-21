from calendar import monthrange
from datetime import date, timedelta
from random import randint

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
from apps.cars.models import Car, Currency


def generate_data():
    cars = Car.objects.all()
    currencies = Currency.objects.all()

    today = date.today()

    for car in cars:
        for month_offset in range(3):  # Current month + next 2 months
            year, month = (today.year, today.month + month_offset)
            if month > 12:
                year += 1
                month -= 12

            first_day = date(year, month, 1)
            last_day = date(year, month, monthrange(year, month)[1])

            # Generate CarPrice for each week in the month
            current_date = first_day
            while current_date <= last_day:
                # Ensure from_date is a Saturday
                from_date = current_date
                while from_date.weekday() != 5:  # Saturday
                    from_date += timedelta(days=1)

                # Ensure to_date is the next Friday
                to_date = from_date + timedelta(days=6)

                # Make sure we don't go past the month's last day
                if to_date > last_day:
                    break

                car_price = CarPriceFactory(car=car, from_date=from_date, to_date=to_date)

                for currency in currencies:
                    CarLocalPriceFactory(car_price=car_price, currency=currency)

                # Move to the next week
                current_date = to_date + timedelta(days=1)

        rental_packages = [RentalPackageFactory(car=car, is_default=i == 0) for i in range(2)]

        for package in rental_packages:
            addons = [RentalAddonFactory() for _ in range(randint(5, 8))]
            package.addons.add(*addons)
            for addon in addons:
                for currency in currencies:
                    RentalAddonLocalPriceFactory(addon=addon, currency=currency)


class Command(BaseCommand):
    help = "Generate sample data for car rental models using Factory Boy"

    def handle(self, *args, **kwargs):

        CurrencyFactory.create_batch(4)
        LocationFactory.create_batch(4)
        CompanyFactory.create_batch(2)
        CarFactory.create_batch(10)

        generate_data()

        self.stdout.write(self.style.SUCCESS(
            "Sample data has been generated successfully using Factory Boy!"
        ))
