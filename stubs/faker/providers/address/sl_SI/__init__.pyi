from .. import Provider as AddressProvider
from _typeshed import Incomplete

class Provider(AddressProvider):
    city_formats: Incomplete
    street_name_formats: Incomplete
    street_address_formats: Incomplete
    address_formats: Incomplete
    building_number_formats: Incomplete
    postcode_formats: Incomplete
    cities: Incomplete
    streets: Incomplete
    states: Incomplete
    countries: Incomplete
    def city_name(self) -> str: ...
    def street_name(self) -> str: ...
    def administrative_unit(self) -> str: ...
    state = administrative_unit
