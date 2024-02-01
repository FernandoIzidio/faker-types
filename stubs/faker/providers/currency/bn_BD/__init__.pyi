from .. import Provider as CurrencyProvider
from _typeshed import Incomplete
from faker.providers.person.bn_BD import translate_to_bengali_digits as translate_to_bengali_digits

class Provider(CurrencyProvider):
    currencies: Incomplete
    cryptocurrencies: Incomplete
    def pricetag(self) -> str: ...
