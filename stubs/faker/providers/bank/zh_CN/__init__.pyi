from .. import Provider as BankProvider
from _typeshed import Incomplete

class Provider(BankProvider):
    banks: Incomplete
    def bank(self) -> str: ...
