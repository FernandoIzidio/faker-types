from .. import Provider as AddressProvider
from _typeshed import Incomplete

class Provider(AddressProvider):
    city_formats: Incomplete
    building_number_formats: Incomplete
    postcode_formats: Incomplete
    section_formats: Incomplete
    street_address_formats: Incomplete
    address_formats: Incomplete
    secondary_address_formats: Incomplete
    street_names: Incomplete
    street_suffixes: Incomplete
    cities: Incomplete
    city_suffixes: Incomplete
    countries: Incomplete
    def secondary_address(self) -> str: ...
    def building_number(self) -> str: ...
    def street_name(self) -> str: ...
    def street_name_suffix(self) -> str: ...
    def city_name(self) -> str: ...
    def city_name_suffix(self) -> str: ...
    def section_number(self) -> str: ...
