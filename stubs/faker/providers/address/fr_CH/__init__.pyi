from .. import Provider as AddressProvider
from _typeshed import Incomplete
from typing import Tuple

class Provider(AddressProvider):
    city_suffixes: Incomplete
    city_prefixes: Incomplete
    street_prefixes: Incomplete
    address_formats: Incomplete
    building_number_formats: Incomplete
    city_formats: Incomplete
    street_address_formats: Incomplete
    street_name_formats: Incomplete
    postcode_formats: Incomplete
    cantons: Incomplete
    countries: Incomplete
    def street_prefix(self) -> str: ...
    def city_prefix(self) -> str: ...
    def canton(self) -> Tuple[str, str]: ...
    def administrative_unit(self) -> str: ...
    canton_name = administrative_unit
    def canton_code(self) -> str: ...
