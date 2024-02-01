from ..de import Provider as AddressProvider
from _typeshed import Incomplete

class Provider(AddressProvider):
    city_formats: Incomplete
    city_with_postcode_formats: Incomplete
    street_name_formats: Incomplete
    street_address_formats: Incomplete
    address_formats: Incomplete
    building_number_formats: Incomplete
    street_suffixes_long: Incomplete
    street_suffixes_short: Incomplete
    postcode_formats: Incomplete
    cities: Incomplete
    states: Incomplete
    def street_suffix_short(self) -> str: ...
    def street_suffix_long(self) -> str: ...
    def city_name(self) -> str: ...
    def administrative_unit(self) -> str: ...
    state = administrative_unit
    def city_with_postcode(self) -> str: ...
