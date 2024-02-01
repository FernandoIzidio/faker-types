from .. import Provider as AddressProvider
from _typeshed import Incomplete

class Provider(AddressProvider):
    building_number_formats: Incomplete
    street_name_formats: Incomplete
    street_address_formats: Incomplete
    street_prefixes: Incomplete
    street_suffixes: Incomplete
    address_formats: Incomplete
    postcode_formats: Incomplete
    city_formats: Incomplete
    cities: Incomplete
    countries: Incomplete
    states: Incomplete
    def street_prefix(self) -> str: ...
    def city_name(self) -> str: ...
    def administrative_unit(self) -> str: ...
    state = administrative_unit
