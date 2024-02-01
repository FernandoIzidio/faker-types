from .. import Provider as BankProvider
from _typeshed import Incomplete

class Provider(BankProvider):
    bban_format: str
    country_code: str
    first_place: Incomplete
    second_place: Incomplete
    swift_location_codes: Incomplete
