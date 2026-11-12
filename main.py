
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
