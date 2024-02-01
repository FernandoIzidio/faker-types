from .. import Provider as AddressProvider
from _typeshed import Incomplete

def getcities(fulldict): ...

class Provider(AddressProvider):
    cap_city_province: Incomplete
    city_prefixes: Incomplete
    city_suffixes: Incomplete
    building_number_formats: Incomplete
    street_suffixes: Incomplete
    postcode_formats: Incomplete
    cities: Incomplete
    states: Incomplete
    states_abbr: Incomplete
    countries: Incomplete
    city_formats: Incomplete
    street_name_formats: Incomplete
    street_address_formats: Incomplete
    address_formats: Incomplete
    secondary_address_formats: Incomplete
    def postcode_city_province(self) -> str: ...
    def city(self) -> str: ...
    def city_prefix(self) -> str: ...
    def secondary_address(self) -> str: ...
    def administrative_unit(self) -> str: ...
    state = administrative_unit
    def state_abbr(self) -> str: ...
