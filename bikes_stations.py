class Bicycle:
    def __init__(self, bike_number: int, electric: bool = False, charge: int = 100):
        if electric and not 0 <= charge <= 100:
            raise ValueError("Заряд має бути від 0 до 100")

        self.bike_number = bike_number
        self.electric = electric
        self.charge = charge if electric else None

    def rate(self) -> int:
        return 5 if self.electric else 2

    def can_ride(self) -> bool:
        return self.charge is None or self.charge >= 20


class Station:
    def __init__(self, name: str, bikes: list[Bicycle]):
        self.name = name
        self.bikes = list(bikes)

    def find_bicycle(self, bike_number: int) -> Bicycle | None:
        for bike in self.bikes:
            if bike.bike_number == bike_number:
                return bike
        return None

    def find_ready_bike(self) -> Bicycle | None:
        for bike in self.bikes:
            if bike.can_ride():
                return bike
        return None

    def take_bicycle(self, bike: Bicycle) -> None:
        self.bikes.remove(bike)

    def return_bicycle(self, bike: Bicycle) -> None:
        self.bikes.append(bike)

    def count(self) -> int:
        return len(self.bikes)
