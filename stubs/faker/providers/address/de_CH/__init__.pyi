from ..de import Provider as AddressProvider
from _typeshed import Incomplete
from typing import Tuple

class Provider(AddressProvider):
    city_formats: Incomplete
    building_number_formats: Incomplete
    street_suffixes: Incomplete
    street_name_formats: Incomplete
    street_address_formats: Incomplete
    address_formats: Incomplete
    postcode_formats: Incomplete
    cities: Incomplete
    cantons: Incomplete
    def canton(self) -> Tuple[str, str]: ...
    def city_name(self) -> str: ...
    def administrative_unit(self) -> str: ...
    canton_name = administrative_unit
    def canton_code(self) -> str: ...
