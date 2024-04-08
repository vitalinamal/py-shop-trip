import json

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:

    with open("app/config.json", "r") as file:
        config = json.load(file)
    fuel_price = config["FUEL_PRICE"]

    shops = [Shop(**shop) for shop in config["shops"]]
    customers = [Customer(**{**customer, "car": Car(**customer["car"])})
                 for customer in config["customers"]]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        cheapest_shop = None
        minimum_total_cost = float("inf")

        for shop in shops:
            trip_cost = customer.calculate_trip_cost(shop.location, fuel_price)
            products_cost = shop.calculate_products_cost(customer.product_cart)
            total_cost = trip_cost + products_cost

            print(f"{customer.name}'s trip to the {shop.name} "
                  f"costs {total_cost:.2f}")

            if total_cost < customer.money and total_cost < minimum_total_cost:
                cheapest_shop = shop
                minimum_total_cost = total_cost

        if cheapest_shop and customer.money >= minimum_total_cost:
            products_cost = cheapest_shop.calculate_products_cost(
                customer.product_cart
            )
            customer.money -= minimum_total_cost
            print(f"{customer.name} rides to {cheapest_shop.name}")
            cheapest_shop.print_receipt(
                customer.name,
                customer.product_cart,
                products_cost
            )
            print(f"{customer.name} rides home")
            print(f"{customer.name} now has {customer.money:.2f} dollars\n")
        else:
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop")
