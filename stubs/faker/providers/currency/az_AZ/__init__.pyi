from .. import Provider as CurrencyProvider
from _typeshed import Incomplete

class Provider(CurrencyProvider):
    currencies: Incomplete
    price_formats: Incomplete
    def pricetag(self): ...
