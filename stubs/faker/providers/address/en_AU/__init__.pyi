from ..en import Provider as AddressProvider
from _typeshed import Incomplete

class Provider(AddressProvider):
    city_prefixes: Incomplete
    city_suffixes: Incomplete
    building_number_formats: Incomplete
    street_suffixes: Incomplete
    postcode_formats: Incomplete
    states: Incomplete
    states_abbr: Incomplete
    city_formats: Incomplete
    street_name_formats: Incomplete
    street_address_formats: Incomplete
    address_formats: Incomplete
    secondary_address_formats: Incomplete
    def city_prefix(self) -> str: ...
    def secondary_address(self) -> str: ...
    def administrative_unit(self) -> str: ...
    state = administrative_unit
    def state_abbr(self) -> str: ...
