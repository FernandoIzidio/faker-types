from .. import Provider as PhoneNumberProvider
from _typeshed import Incomplete

class Provider(PhoneNumberProvider):
    formats: Incomplete
    area_codes: Incomplete
    def area_code(self) -> str: ...
    def phone_number(self) -> str: ...
