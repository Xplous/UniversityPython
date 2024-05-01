
class Wallet:
    payment_system = "МИР"
    def __init__(self, name, currency):
        self.name = name
        self._balance = 0
        if currency in ("USD", "EUR", "RUB"):
            self.currency = currency
        else:
            raise ValueError("Не поддерживаемая валюта")

    def top_up_balance(self, amount):
        self._balance += amount
        print(f"Баланс был увеличен. Новый баланс: {self._balance} {self.currency}")

    def make_payment(self, amount):
        if self._balance >= amount:
            self._balance -= amount
            print(f"Платёж на сумму {amount} {self.currency} произошёл успешно. Оставшийся баланс: {self._balance} {self.currency}")
        else:
            print("Недостаточно средств для совершения платежа")

    def get_balance_info(self):
        print(f"Текущий баланс: {self._balance} {self.currency}")

    def close_account(self):
        del self
        print("Кошелёк был закрыт")


class CryptoWallet(Wallet):
    def __init__(self, name, currency, coin):
        super().__init__(name, currency)
        self.coin = coin

    def get_balance_info(self):
        print(f"Текущий баланс: {self._balance} {self.coin}")

    def get_balance_in_usd(self, btc_price=72000, eth_price=3500):
        if self.coin == "BTC":
            balance_usd = self._balance * btc_price
        elif self.coin == "ETH":
            balance_usd = self._balance * eth_price
        else:
            balance_usd = 0
        print(f"Текущий баланс: {balance_usd} {self.currency}")


# Пример использования:

# Банковский кошелёк
wallet1 = Wallet("XPLOUS WALLET", "RUB")
wallet1.top_up_balance(500)
wallet1.make_payment(200)
wallet1.get_balance_info()

# Крипто кошелёк с битками
crypto_wallet1 = CryptoWallet("XPLOUS CRYPTA WALLET", "RUB", "BTC")
crypto_wallet1.top_up_balance(1)
crypto_wallet1.get_balance_info()
crypto_wallet1.get_balance_in_usd()

