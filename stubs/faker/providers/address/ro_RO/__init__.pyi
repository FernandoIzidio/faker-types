from .. import Provider as AddressProvider
from _typeshed import Incomplete
from typing import Tuple

class Provider(AddressProvider):
    street_prefixes: Incomplete
    street_name_formats: Incomplete
    street_address_formats: Incomplete
    address_formats: Incomplete
    building_number_formats: Incomplete
    secondary_address_formats: Incomplete
    postcode_formats: Incomplete
    city_formats: Incomplete
    cities: Incomplete
    states: Tuple[Tuple[str, str], ...]
    def street_prefix(self) -> str: ...
    def secondary_address(self) -> str: ...
    def city_name(self) -> str: ...
    def city_with_postcode(self) -> str: ...
    def administrative_unit(self) -> str: ...
    state = administrative_unit
    def state_abbr(self) -> str: ...
