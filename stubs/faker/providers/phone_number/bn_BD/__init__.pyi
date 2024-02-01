from .. import Provider as PhoneNumberProvider
from _typeshed import Incomplete
from faker.providers.person.bn_BD import translate_to_bengali_digits as translate_to_bengali_digits

class Provider(PhoneNumberProvider):
    country_calling_codes: Incomplete
    formats: Incomplete
    def phone_number(self) -> str: ...
    def msisdn(self) -> str: ...
