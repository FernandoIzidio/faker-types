from .. import Provider as CurrencyProvider
from _typeshed import Incomplete

class Provider(CurrencyProvider):
    price_formats: Incomplete
    def pricetag(self) -> str: ...
