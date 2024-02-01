from .. import Provider as AddressProvider
from _typeshed import Incomplete

class Provider(AddressProvider):
    city_suffixes: Incomplete
    street_suffixes: Incomplete
    city_formats: Incomplete
    street_name_formats: Incomplete
    street_address_formats: Incomplete
    address_formats: Incomplete
    building_number_formats: Incomplete
    building_number_suffixes: Incomplete
    postcode_formats: Incomplete
    def building_number(self) -> str: ...
    def city_suffix(self) -> str: ...
    def street_suffix(self) -> str: ...
