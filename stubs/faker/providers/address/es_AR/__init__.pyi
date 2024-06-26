from ..es import Provider as AddressProvider
from _typeshed import Incomplete
from typing import List, Tuple

class Provider(AddressProvider):
    provinces: Incomplete
    municipalities: List[Tuple[str, str, str]]
    street_prefixes: Incomplete
    street_suffixes: Incomplete
    street_proceres: Incomplete
    street_name_formats: Incomplete
    building_number_formats: Incomplete
    secondary_address_formats: Incomplete
    postcode_formats: Incomplete
    def provinces_code(self) -> str: ...
    def province(self) -> str: ...
    administrative_unit = province
    def municipality_code(self) -> str: ...
    def municipality(self) -> str: ...
    city = municipality
    def street_prefix(self) -> str: ...
    def street_procer(self) -> str: ...
    def street_municipality(self) -> str: ...
    def street_province(self) -> str: ...
    def street_suffix(self) -> str: ...
    def street_name(self) -> str: ...
    def building_number(self) -> str: ...
    def secondary_address(self) -> str: ...
    def street_address(self) -> str: ...
    def postcode(self) -> str: ...
    def address(self) -> str: ...
