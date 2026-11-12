
from bikes_stations import Bicycle, Station
from client import Client
from rental import return_bicycle, take_bicycle
def ride(
    client: Client,
    start: Station,
    end: Station,
    bike_number: int,
    minutes: int,
    deposit_sum: int,
) -> int:
    message = take_bicycle(client, start, bike_number, deposit_sum)
    if message is not None:
        raise RuntimeError(message)
    cost = return_bicycle(client, end, minutes)
    print(f"{client.name} їде з {start.name} на {end.name} {minutes} хв і платить {cost} грн")
    return cost
def print_report(stations: list[Station], total: int) -> None:
    print("Звіт адміністратора")
    for station in stations:
        print(f"Станція {station.name} {station.count()}велосипедів")
    print(f"Виручка {total} грн")
def main() -> None:
    a = Station("А", [Bicycle(1), Bicycle(2), Bicycle(3, electric=True)])
    b = Station("Б", [Bicycle(4, electric=True)])
    maryam = Client("Марьям", 200)
    albek = Client("Альбек", 100)
    deposit_sum = 50

    total = ride(maryam, a, b, 3, 20, deposit_sum)
    total += ride(albek, a, b, 1, 10, deposit_sum)
    total += ride(maryam, a, b, 2, 15, deposit_sum)
    message = take_bicycle(albek, a, 1, deposit_sum)
    assert message == "На станції А немає велосипедів" and albek.balance == 80
    print(message)
    print(f"Баланс Марьям  {maryam.balance} грн")
    print(f"Баланс Альбека {albek.balance} грн")
    assert (maryam.balance, albek.balance, total) == (70, 80, 150)
    print_report([a, b], total)
    print("Перевірка боргу і поповнення")
    total += ride(maryam, b, a, 3, 20, deposit_sum)
    print(f"Баланс Марьям {maryam.balance} грн")
    message = take_bicycle(maryam, a, 3, deposit_sum)
    assert message == "Спочатку потрібно поповнити баланс"
    print(message)
    maryam.top_up(100)
    print(f"Після поповнення баланс — {maryam.balance} грн")
    message = take_bicycle(maryam, a, 3, deposit_sum)
    if message is not None:
        raise RuntimeError(message)
    print("Марьям знову може взяти велосипед")
    total += return_bicycle(maryam, a, 1)
    print_report([a, b], total)

