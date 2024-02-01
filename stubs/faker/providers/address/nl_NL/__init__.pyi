from .. import Provider as AddressProvider
from _typeshed import Incomplete

class Provider(AddressProvider):
    building_number_formats: Incomplete
    street_suffixes: Incomplete
    postcode_formats: Incomplete
    city_formats: Incomplete
    countries: Incomplete
    cities: Incomplete
    provinces: Incomplete
    street_name_formats: Incomplete
    street_address_formats: Incomplete
    address_formats: Incomplete
    def administrative_unit(self) -> str: ...
    province = administrative_unit
    def city(self) -> str: ...
