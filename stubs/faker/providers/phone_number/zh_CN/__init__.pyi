from .. import Provider as PhoneNumberProvider
from _typeshed import Incomplete

class Provider(PhoneNumberProvider):
    phonenumber_prefixes: Incomplete
    formats: Incomplete
    def phonenumber_prefix(self) -> int: ...
