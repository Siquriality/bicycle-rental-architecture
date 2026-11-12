from decimal import Decimal

from bikes_stations import Bicycle
from deposit import Deposit


class Client:

    def __init__(self, name: str, balance: int):
        self.name = name
        self.balance = Decimal(balance)
        self.bike: Bicycle | None = None
        self.deposit: Deposit | None = None
        self.trips = 0


    def charge(self, money: Decimal) -> None:
        self.balance -= money


    def top_up(self, money: Decimal) -> None:
        if money <= 0:
            raise ValueError("Сума поповнення має бути більшою за нуль")
        self.balance += money
