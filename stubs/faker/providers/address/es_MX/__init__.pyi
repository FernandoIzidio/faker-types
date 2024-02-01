from ..es import Provider as AddressProvider
from _typeshed import Incomplete

class Provider(AddressProvider):
    city_prefixes: Incomplete
    city_adjectives: Incomplete
    city_suffixes: Incomplete
    street_prefixes: Incomplete
    building_number_formats: Incomplete
    postcode_formats: Incomplete
    states: Incomplete
    zip_codes: Incomplete
    city_formats: Incomplete
    street_name_formats: Incomplete
    street_address_formats: Incomplete
    address_formats: Incomplete
    secondary_address_formats: Incomplete
    def city_prefix(self) -> str: ...
    def city_suffix(self) -> str: ...
    def city_adjective(self) -> str: ...
    def street_prefix(self) -> str: ...
    def secondary_address(self) -> str: ...
    def administrative_unit(self) -> str: ...
    state = administrative_unit
    def state_abbr(self) -> str: ...
