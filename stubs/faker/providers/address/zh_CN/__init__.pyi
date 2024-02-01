from .. import Provider as AddressProvider
from _typeshed import Incomplete

class Provider(AddressProvider):
    city_suffixes: Incomplete
    city_formats: Incomplete
    district_formats: Incomplete
    building_number_formats: Incomplete
    postcode_formats: Incomplete
    street_suffixes: Incomplete
    street_name_formats: Incomplete
    street_address_formats: Incomplete
    address_formats: Incomplete
    provinces: Incomplete
    districts: Incomplete
    cities: Incomplete
    countries: Incomplete
    def building_number(self) -> str: ...
    def city_name(self) -> str: ...
    def administrative_unit(self) -> str: ...
    province = administrative_unit
    def district(self) -> str: ...
