from datetime import timedelta

import factory
from apps.cars.models import (
    Company,
    Location,
    Currency,
    CurrencyConversion,
    Car,
    CarPrice,
    CarLocalPrice,
    RentalAddon,
    RentalPackage,
    RentalAddonLocalPrice
)
import random
from faker import Faker


fake = Faker()

class CurrencyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Currency

    name = factory.Faker('currency_name')
    code = factory.Faker('currency_code')


class LocationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Location

    name = factory.Faker('city')
    lat = factory.Faker('latitude')
    long = factory.Faker('longitude')


class CompanyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Company

    name = factory.Faker('company')
    address = factory.Faker('address')


class CarFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Car

    company = factory.SubFactory(CompanyFactory)
    name = factory.Faker('company')
    from_location = factory.SubFactory(LocationFactory)
    to_location = factory.SubFactory(LocationFactory)


class CarPriceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CarPrice

    car = factory.SubFactory(CarFactory)
    base_currency = factory.Iterator(Currency.objects.all())

    @factory.lazy_attribute
    def from_date(self):
        # Get a random date this month
        random_date = fake.date_this_month()
        # Calculate days to subtract to reach previous Saturday
        weekday = random_date.weekday()
        days_to_subtract = (weekday + 1) % 7
        # Return the adjusted Saturday date
        return random_date - timedelta(days=days_to_subtract+1)

    @factory.lazy_attribute
    def to_date(self):
        # Add 6 days to from_date to get to Friday
        return self.from_date + timedelta(days=6)

    base_price = factory.LazyAttribute(lambda x: round(random.uniform(100, 500), 2))
    discount_rate = factory.LazyAttribute(lambda x: round(random.uniform(0, 0.2), 2))


class CarLocalPriceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CarLocalPrice

    car_price = factory.SubFactory(CarPriceFactory)
    local_price = factory.LazyAttribute(lambda x: x.car_price.base_price * (1 + random.uniform(-0.1, 0.1)))
    currency = factory.Iterator(Currency.objects.all())
    exchange_rate = factory.LazyAttribute(lambda x: random.uniform(0.8, 1.2))


class RentalAddonFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = RentalAddon

    name = factory.Faker('word')
    is_mandatory = factory.Faker('boolean')
    price = factory.LazyAttribute(lambda x: random.uniform(5, 20))
    currency = factory.Iterator(Currency.objects.all())
    pricing_unit = factory.Faker('word')


class RentalPackageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = RentalPackage

    name = factory.Faker('company')
    car = factory.SubFactory(CarFactory)
    is_default = factory.Faker('boolean')


class RentalAddonLocalPriceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = RentalAddonLocalPrice

    addon = factory.SubFactory(RentalAddonFactory)
    local_price = factory.LazyAttribute(lambda x: x.addon.price * (1 + random.uniform(-0.1, 0.1)))
    currency = factory.Iterator(Currency.objects.all())
    exchange_rate = factory.LazyAttribute(lambda x: random.uniform(0.8, 1.2))
