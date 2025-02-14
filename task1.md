# API endpoint to list all the cars

## API description: 
This API will list all the cars available in the system. The cars will be filtered based on the query parameters. The cars will be paginated based on the `page` and `page_size` query parameters.

### Endpoint: 
`GET /api/v1/cars/`

### Query Parameters:
- `page` (optional): The page number to fetch. Default is 1.
- `page_size` (optional): The number of items to fetch per page. Default is 10.
- `from_date` (required): The start date to filter the cars.
  - Format: `YYYY-MM-DD`
  - Example: `2021-01-01`
  - Description: If price is set for a car for a week, then the car should be listed if the `from_date` falls within the week. The `from_date` will be the Saturday of the week.
- `to_date` (required): The end date to filter the cars.
  - Format: `YYYY-MM-DD`
  - Example: `2021-01-07`
  - Description: If price is set for a car for a week, then the car should be listed if the `to_date` falls within the week. The `to_date` will be the Friday of the week. 
  - Note: Max 4 weeks difference between `from_date` and `to_date`.
- `from_location` (optional): The start location to filter the cars.
  - Example: `Kathmandu`
  - Description: The car should be listed if the `from_location` matches the car's location.
- `to_location` (optional): The end location to filter the cars.
  - Example: `Pokhara`
  - Description: The car should be listed if the `to_location` matches the car's location.
- `currency` (optional): The currency to filter the cars.
  - Example: `USD`

### Response:
```json
{
  "count": 10,
  "next": "http://localhost:8000/api/v1/cars/?page=2",
  "previous": null,
  "results": [
    {
      "id": 1,
      "name": "Toyota Corolla",
      "company": {
        "id": 1,
        "name": "ABC Car Rental"
      },
      "from_location": "Kathmandu",
      "to_location": "Pokhara",
      "from_date": "2021-01-01",
      "to_date": "2021-01-07",
      "packages": [
        {
          "name": "Standard",
          "is_default": true,
          "total_additional_price": 10,
          "addons": [
            {
              "name": "GPS",
              "price": 10,
              "currency": "USD"
            }
          ]
        }
      ],
      "price": {
          "base_price": 100,
          "discounted_price": 90,
          "discount": 10,
          "discount_percentage": 10,
          "currency": "USD"
      }
    }
  ]
}
```

### Response Description:
- `packages`: The list of rental packages available for the car.
  - `total_additional_price`: The total accumulated price of all the addons.
- `price`: The pricing details of the car.
  - `base_price`: The total accumulated base_price in given date range and currency.
  - `discounted_price`: The discounted price of the car.
  - `discount`: The discount amount.
  - `discount_percentage`: The discount percentage.
  - `currency`: The currency of the price.
  - Note: The price will be calculated based on the `from_date` and `to_date` query parameters.
  - Example: 
    - Assume the car has the following prices and discounts rates:
      - `2024-01-06` (Saturday) to `2024-01-12` (Friday): 
        - price: `USD 100`
        - discount_rate: `10%`
      - `2024-01-13` (Saturday) to `2024-01-19` (Friday):
        - price: `USD 150`
        - discount_rate: `12%`
    - If the `from_date` is `2024-01-06` and `to_date` is `2024-01-12`, then:
      - `base_price`: `USD 100`
      - `discounted_price`: `USD 90`
      - `discount`: `USD 10`
      - `discount_percentage`: `10`
    - If the `from_date` is `2024-01-06` and `to_date` is `2024-01-19`, then:
      - `base_price`: `USD 250` (USD 100 + USD 150)
      - `discounted_price`: `USD 222` (USD 90 + USD 132)
      - `discount`: `USD 28` (USD 10 + USD 18)
      - `discount_percentage`: `11.2` (28/250 * 100)