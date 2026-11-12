class Deposit:
    def __init__(self, money: int):
        if money <= 0:
            raise ValueError("Депозит має бути більшим за нуль")

        self._amount = money
        self._held = False

    def can_hold(self, balance: int) -> bool:
        return not self._held and balance >= self._amount

    def hold(self, balance: int) -> int:
        if not self.can_hold(balance):
            raise ValueError("Не можна взяти депозит")

        self._held = True
        return balance - self._amount

    def refund(self, balance: int) -> int:
        if not self._held:
            raise ValueError("Немає депозиту для повернення")

        self._held = False
        return balance + self._amount
