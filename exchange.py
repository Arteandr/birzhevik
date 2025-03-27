class Currency:
    """
    Класс для представления валюты.

    Attributes:
        name (str): Название валюты.
        rate (float): Текущий курс валюты по отношению к базовой валюте (USD).
        history (list): История изменений курса.
    """

    def __init__(self, name, initial_rate):
        """
        Инициализирует объект Currency.

        Args:
            name (str): Название валюты.
            initial_rate (float): Начальный курс валюты.
        """
        self.name = name
        self.rate = initial_rate
        self.history = [initial_rate]

    def update_rate(self, new_rate):
        """
        Обновляет курс валюты и добавляет его в историю.

        Args:
            new_rate (float): Новый курс валюты.
        """
        self.rate = new_rate
        self.history.append(new_rate)

    def get_current_rate(self):
        """
        Возвращает текущий курс валюты.

        Returns:
            float: Текущий курс.
        """
        return self.rate


class Exchange:
    """
    Класс для управления курсами обмена между валютами.

    Attributes:
        currencies (dict): Словарь валют, где ключ - название валюты, значение - объект Currency.
        exchange_rates (dict): Словарь курсов обмена, где ключ - кортеж (from_currency, to_currency), значение - курс.
    """

    def __init__(self):
        self.currencies = {}
        self.exchange_rates = {}

    def add_currency(self, currency):
        """
        Добавляет валюту в биржу.

        Args:
            currency (Currency): Объект Currency.
        """
        self.currencies[currency.name] = currency

    def set_exchange_rate(self, from_currency, to_currency, rate):
        """
        Устанавливает курс обмена между двумя валютами.

        Args:
            from_currency (str): Название валюты, из которой обмениваем.
            to_currency (str): Название валюты, в которую обмениваем.
            rate (float): Курс обмена.
        """
        self.exchange_rates[(from_currency, to_currency)] = rate
        self.exchange_rates[(to_currency, from_currency)] = 1 / rate

    def convert(self, amount, from_currency, to_currency):
        """
        Конвертирует сумму из одной валюты в другую.

        Args:
            amount (float): Сумма для конвертации.
            from_currency (str): Название валюты, из которой обмениваем.
            to_currency (str): Название валюты, в которую обмениваем.

        Returns:
            float: Конвертированная сумма.
        """
        if (from_currency, to_currency) in self.exchange_rates:
            return amount * self.exchange_rates[(from_currency, to_currency)]
        else:
            raise ValueError("Курс обмена не установлен для данной пары валют.")


# Пример использования
if __name__ == "__main__":
    # Создаем валюты
    usd = Currency("USD", 1.0)      # Базовая валюта
    rub = Currency("RUB", 75.0)     # Рубли
    cny = Currency("CNY", 7.0)      # Юани
    btc = Currency("BTC", 50000.0)  # Биткоин
    eth = Currency("ETH", 3000.0)   # Эфириум

    # Создаем биржу
    exchange = Exchange()

    # Добавляем валюты в биржу
    exchange.add_currency(usd)
    exchange.add_currency(rub)
    exchange.add_currency(cny)
    exchange.add_currency(btc)
    exchange.add_currency(eth)

    # Устанавливаем курсы обмена
    exchange.set_exchange_rate("RUB", "CNY", 0.093)  # Рубли в юани
    exchange.set_exchange_rate("BTC", "USD", 50000.0)  # Биткоин в доллары
    exchange.set_exchange_rate("ETH", "USD", 3000.0)   # Эфириум в доллары

    # Обновляем курс валюты (движение валют)
    rub.update_rate(80.0)  # Новый курс рубля

    # Примеры конвертации
    print(f"1000 RUB = {exchange.convert(1000, 'RUB', 'CNY')} CNY")
    print(f"1 BTC = {exchange.convert(1, 'BTC', 'USD')} USD")
    print(f"2 ETH = {exchange.convert(2, 'ETH', 'USD')} USD")