from bikes_stations import Bicycle, Station
from client import Client
from deposit import Deposit

def take_bicycle(client: Client, station: Station, bike_number: int, deposit_sum: int):
    if client.bike is not None:
        return "Клієнт уже орендує велосипед"
    if client.balance < 0:
        return "Спочатку потрібно поповнити баланс"
    if station.count() == 0:
        return f"На станції {station.name} немає велосипедів"

    bike = station.find_bicycle(bike_number)
    if bike is None:
        return f"На станції {station.name} немає велосипеда №{bike_number}"

    deposit = Deposit(deposit_sum)
    if not deposit.can_hold(client.balance):
        return "На балансі не вистачає грошей на депозит"

    client.balance = deposit.hold(client.balance)
    station.take_bicycle(bike)
    client.bike = bike
    client.deposit = deposit
    return None


def calculate_cost(bike: Bicycle, minutes: int):
    if minutes <= 0:
        raise ValueError("Тривалість поїздки має бути більшою за нуль")
    return bike.rate() * minutes


def return_bicycle(client: Client, station: Station, minutes: int):
    bike = client.bike
    deposit = client.deposit
    if bike is None or deposit is None:
        raise ValueError("Клієнт не орендує велосипед")

    cost = calculate_cost(bike, minutes)
    client.balance = deposit.refund(client.balance)
    client.charge(cost)
    station.return_bicycle(bike)
    client.bike = None
    client.deposit = None
    return cost


