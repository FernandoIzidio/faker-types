from ..en import Provider as AddressProvider
from _typeshed import Incomplete

class Provider(AddressProvider):
    city_prefixes: Incomplete
    city_suffixes: Incomplete
    counties: Incomplete
    building_number_formats: Incomplete
    street_suffixes: Incomplete
    POSTAL_ZONES: Incomplete
    POSTAL_ZONES_ONE_CHAR: Incomplete
    POSTAL_ZONES_TWO_CHARS: Incomplete
    postcode_formats: Incomplete
    city_formats: Incomplete
    street_name_formats: Incomplete
    street_address_formats: Incomplete
    address_formats: Incomplete
    secondary_address_formats: Incomplete
    def postcode(self) -> str: ...
    def city_prefix(self) -> str: ...
    def secondary_address(self) -> str: ...
    def administrative_unit(self) -> str: ...
    county = administrative_unit
