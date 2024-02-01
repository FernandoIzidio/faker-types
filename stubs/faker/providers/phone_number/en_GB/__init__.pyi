from .. import Provider as PhoneNumberProvider
from _typeshed import Incomplete

class Provider(PhoneNumberProvider):
    cellphone_formats: Incomplete
    formats: Incomplete
    def cellphone_number(self) -> str: ...
