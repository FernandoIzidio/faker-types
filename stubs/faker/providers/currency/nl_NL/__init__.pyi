from _typeshed import Incomplete
from faker.providers.currency import Provider as CurrencyProvider

class Provider(CurrencyProvider):
    price_formats: Incomplete
    def pricetag(self) -> str: ...
