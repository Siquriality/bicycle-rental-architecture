
from decimal import Decimal
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
) -> Decimal:
    message = take_bicycle(client, start, bike_number, deposit_sum)
    if message is not None:
        raise RuntimeError(message)
    bike = client.bike
    assert bike is not None
    if bike.bike_number != bike_number:
        print(f"Замість велосипеда №{bike_number} видали №{bike.bike_number}")
    cost = return_bicycle(client, end, minutes)
    print(f"{client.name} їде з {start.name} на {end.name} {minutes} хв і платить {cost:.2f} грн")
    return cost
def print_report(stations: list[Station], clients: list[Client], total: Decimal) -> None:
    print("Звіт адміністратора")
    for station in stations:
        print(f"Станція {station.name} велосипедів {station.count()}")
    print(f"Виручка {total:.2f} грн")
    print("Електровелосипеди з низьким зарядом")
    for station in stations:
        for bike in station.bikes:
            if not bike.can_ride():
                print(f"№{bike.bike_number} станція {station.name} заряд {bike.charge}%")
    print("Кількість поїздок")
    for client in clients:
        print(f"{client.name} — {client.trips}")
def main() -> None:
    a = Station("А", [Bicycle(1), Bicycle(2), Bicycle(3, electric=True, charge=20)])
    b = Station("Б", [Bicycle(4, electric=True, charge=15)])
    maryam = Client("Марьям", 200)
    albek = Client("Альбек", 100)
    deposit_sum = 50
    message = take_bicycle(albek, b, 4, deposit_sum)
    assert message == "На станції Б немає придатних велосипедів" and albek.balance == 100
    print(message)
    total = ride(maryam, a, b, 3, 20, deposit_sum)
    total += ride(albek, a, b, 1, 10, deposit_sum)
    total += ride(maryam, a, b, 2, 15, deposit_sum)
    message = take_bicycle(albek, a, 1, deposit_sum)
    assert message == "На станції А немає велосипедів" and albek.balance == 80
    print(message)
    print(f"Баланс Марьям — {maryam.balance:.2f} грн")
    print(f"Баланс Альбека — {albek.balance:.2f} грн")
    assert (maryam.balance, albek.balance, total) == (70, 80, 150)
    print_report([a, b], [maryam, albek], total)
    print("Перевірка боргу і поповнення")
    total += ride(maryam, b, a, 4, 20, deposit_sum)
    print(f"Баланс Марьям — {maryam.balance:.2f} грн")
    message = take_bicycle(maryam, a, 3, deposit_sum)
    assert message == "Спочатку потрібно поповнити баланс" and maryam.balance == -30
    print(message)
    maryam.top_up(100)
    print(f"Після поповнення баланс — {maryam.balance:.2f} грн")
    cost = ride(maryam, a, a, 3, 1, deposit_sum)
    assert cost == Decimal("4.50") and maryam.trips == 4
    total += cost
    print_report([a, b], [maryam, albek], total)
if __name__ == "__main__":
    main()
