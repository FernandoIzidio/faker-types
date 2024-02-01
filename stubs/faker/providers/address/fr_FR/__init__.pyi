from .. import Provider as AddressProvider
from _typeshed import Incomplete
from typing import Tuple

class Provider(AddressProvider):
    city_suffixes: Incomplete
    city_prefixes: Incomplete
    street_prefixes: Incomplete
    city_formats: Incomplete
    street_name_formats: Incomplete
    street_address_formats: Incomplete
    address_formats: Incomplete
    building_number_formats: Incomplete
    countries: Incomplete
    regions: Incomplete
    departments: Incomplete
    def street_prefix(self) -> str: ...
    def city_prefix(self) -> str: ...
    def administrative_unit(self) -> str: ...
    region = administrative_unit
    def department(self) -> Tuple[str, str]: ...
    def department_name(self) -> str: ...
    def department_number(self) -> str: ...
    def postcode(self) -> str: ...
