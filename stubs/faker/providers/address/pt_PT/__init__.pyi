from .. import Provider as AddressProvider
from _typeshed import Incomplete

class Provider(AddressProvider):
    street_prefixes: Incomplete
    city_formats: Incomplete
    street_name_formats: Incomplete
    street_address_formats: Incomplete
    address_formats: Incomplete
    building_number_formats: Incomplete
    postcode_formats: Incomplete
    cities: Incomplete
    countries: Incomplete
    distritos: Incomplete
    concelhos: Incomplete
    freguesias: Incomplete
    places: Incomplete
    def street_prefix(self) -> str: ...
    def city_name(self) -> str: ...
    def administrative_unit(self) -> str: ...
    distrito = administrative_unit
    def concelho(self) -> str: ...
    def freguesia(self) -> str: ...
    def place_name(self) -> str: ...
