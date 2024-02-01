from .. import Provider as BankProvider
from _typeshed import Incomplete

class Provider(BankProvider):
    bban_format: str
    country_code: str
    banks: Incomplete
    def bank(self) -> str: ...
