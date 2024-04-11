import json

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        config = json.load(file)

    fuel_price = config["FUEL_PRICE"]
    shops = [Shop(**shop) for shop in config["shops"]]
    customers = [Customer(**customer) for customer in config["customers"]]

    for customer in customers:
        customer.go_shopping(fuel_price, shops)
