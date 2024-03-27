from .. import Provider as PhoneNumberProvider
from _typeshed import Incomplete

class Provider(PhoneNumberProvider):
    cellphone_formats: Incomplete
    telephone_formats: Incomplete
    provider_codes: Incomplete
    start_digits: Incomplete
    area_codes: Incomplete
    formats: Incomplete
    def start_digit(self) -> str: ...
    def provider_code(self) -> str: ...
    def area_code(self) -> str: ...
    def cellphone_number(self) -> str: ...
    def landline_number(self) -> str: ...
    def phone_number(self) -> str: ...