from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=255)
    lat = models.FloatField()
    long = models.FloatField()

    def __str__(self):
        return self.name


class Currency(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class CurrencyConversion(models.Model):
    from_currency = models.ForeignKey(
        "cars.Currency", on_delete=models.CASCADE, related_name='from_currency'
    )
    to_currency = models.ForeignKey(
        "cars.Currency", on_delete=models.CASCADE, related_name='to_currency'
    )
    exchange_rate = models.FloatField()


class Car(models.Model):
    company = models.ForeignKey('cars.Company', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True, blank=True)
    from_location = models.ForeignKey(
        "cars.Location", on_delete=models.CASCADE, related_name='cars_from_location'
    )
    to_location = models.ForeignKey(
        "cars.Location", on_delete=models.CASCADE, related_name='cars_to_location'
    )

    def __str__(self):
        return self.name


class CarPrice(models.Model):
    car = models.ForeignKey(
        "cars.Car", on_delete=models.CASCADE, related_name='car_prices'
    )
    from_date = models.DateField()
    to_date = models.DateField()
    base_price = models.FloatField()
    base_currency = models.ForeignKey(
        "cars.Currency", on_delete=models.CASCADE, related_name='car_prices'
    )
    discount_rate = models.FloatField()

    def __str__(self):
        return f"{self.car.name} - {self.from_date} - {self.to_date}"


class CarLocalPrice(models.Model):
    car_price = models.ForeignKey(
        "cars.CarPrice", on_delete=models.CASCADE, related_name='car_local_prices'
    )
    local_price = models.FloatField()
    currency = models.ForeignKey(
        "cars.Currency", on_delete=models.CASCADE, related_name='car_local_prices'
    )
    exchange_rate = models.FloatField()

    def __str__(self):
        return f"{self.car_price.car.name} - {self.currency.code} - {self.local_price}"


class RentalAddon(models.Model):
    name = models.CharField(max_length=255)
    is_mandatory = models.BooleanField(default=False)
    price = models.FloatField()
    currency = models.ForeignKey(
        "cars.Currency", on_delete=models.CASCADE, related_name='rental_addons'
    )
    pricing_unit = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class RentalPackage(models.Model):
    name = models.CharField(max_length=255)
    car = models.ForeignKey(
        "cars.Car", on_delete=models.CASCADE, related_name='car_rental_packages'
    )
    is_default = models.BooleanField(default=False)
    addons = models.ManyToManyField(
        "cars.RentalAddon", related_name='rental_packages'
    )

    def __str__(self):
        return self.name


class RentalAddonLocalPrice(models.Model):
    addon = models.ForeignKey(
        "cars.RentalAddon",
        on_delete=models.CASCADE,
        related_name='rental_addon_local_prices'
    )
    local_price = models.FloatField()
    currency = models.ForeignKey(
        "cars.Currency",
        on_delete=models.CASCADE,
        related_name='rental_addon_local_prices'
    )
    exchange_rate = models.FloatField()

    def __str__(self):
        return f"{self.addon.name} - {self.currency.code} - {self.local_price}"