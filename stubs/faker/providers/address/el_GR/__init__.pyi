from .. import Provider as AddressProvider
from _typeshed import Incomplete

class Provider(AddressProvider):
    building_number_formats: Incomplete
    street_prefixes_short: Incomplete
    street_prefixes_long: Incomplete
    street_name_formats: Incomplete
    street_address_formats: Incomplete
    postcode_formats: Incomplete
    address_formats: Incomplete
    line_address_formats: Incomplete
    def line_address(self) -> str: ...
    def street_prefix(self) -> str: ...
    def street_prefix_short(self) -> str: ...
    def street_prefix_long(self) -> str: ...
    def street(self) -> str: ...
    def city(self) -> str: ...
    def administrative_unit(self) -> str: ...
    region = administrative_unit
    cities: Incomplete
    regions: Incomplete
    countries: Incomplete
    localities: Incomplete
