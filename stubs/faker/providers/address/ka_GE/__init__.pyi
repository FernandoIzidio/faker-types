from .. import Provider as AddressProvider
from _typeshed import Incomplete

class Provider(AddressProvider):
    city_formats: Incomplete
    street_name_formats: Incomplete
    street_address_formats: Incomplete
    address_formats: Incomplete
    building_number_formats: Incomplete
    street_suffixes: Incomplete
    countries: Incomplete
    street_titles: Incomplete
    city_names: Incomplete
    def street_title(self) -> str: ...
    def city_name(self) -> str: ...
