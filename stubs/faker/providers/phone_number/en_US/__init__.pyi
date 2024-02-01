from .. import Provider as PhoneNumberProvider
from _typeshed import Incomplete

class Provider(PhoneNumberProvider):
    formats: Incomplete
    basic_formats: Incomplete
    def basic_phone_number(self) -> str: ...
