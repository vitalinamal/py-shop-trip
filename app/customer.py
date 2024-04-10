from app.car import Car


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list[int],
            money: float,
            car: dict
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = Car(**car)

    def calculate_trip_cost(
            self,
            shop_location: list[int],
            fuel_price: float
    ) -> float:
        distance = (
            ((shop_location[0] - self.location[0]) ** 2)
            + ((shop_location[1] - self.location[1]) ** 2)
        ) ** 0.5
        return self.car.fuel_consumption / 100.0 * distance * fuel_price * 2
