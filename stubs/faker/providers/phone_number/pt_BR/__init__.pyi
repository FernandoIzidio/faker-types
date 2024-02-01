from .. import Provider as PhoneNumberProvider
from _typeshed import Incomplete

class Provider(PhoneNumberProvider):
    formats: Incomplete
    msisdn_formats: Incomplete
    cellphone_formats: Incomplete
    services_phones_formats: Incomplete
    def cellphone_number(self) -> str: ...
    def service_phone_number(self) -> str: ...
