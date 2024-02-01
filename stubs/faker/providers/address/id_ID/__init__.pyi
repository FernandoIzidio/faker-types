from .. import Provider as AddressProvider
from _typeshed import Incomplete

class Provider(AddressProvider):
    building_number_formats: Incomplete
    city_formats: Incomplete
    postcode_formats: Incomplete
    street_name_formats: Incomplete
    street_address_formats: Incomplete
    address_formats: Incomplete
    streets: Incomplete
    street_prefixes_long: Incomplete
    street_prefixes_short: Incomplete
    cities: Incomplete
    states: Incomplete
    states_abbr: Incomplete
    countries: Incomplete
    def street(self) -> str: ...
    def street_prefix_short(self) -> str: ...
    def street_prefix_long(self) -> str: ...
    def city_name(self) -> str: ...
    def administrative_unit(self) -> str: ...
    state = administrative_unit
    def state_abbr(self) -> str: ...
    def country(self) -> str: ...
