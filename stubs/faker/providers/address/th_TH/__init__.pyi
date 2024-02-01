from ..th import Provider as AddressProvider
from _typeshed import Incomplete

class Provider(AddressProvider):
    street_name_formats: Incomplete
    street_address_formats: Incomplete
    address_formats: Incomplete
    city_formats: Incomplete
    cities: Incomplete
    building_number_formats: Incomplete
    street_prefixes: Incomplete
    postcode_formats: Incomplete
    provinces: Incomplete
    amphoes: Incomplete
    tambons: Incomplete
    tambon_prefixes: Incomplete
    tambon_suffixes: Incomplete
    city_suffixes: Incomplete
    def street_prefix(self) -> str: ...
    def administrative_unit(self) -> str: ...
    province = administrative_unit
    def amphoe(self) -> str: ...
    def tambon(self) -> str: ...
    def city_name(self) -> str: ...
