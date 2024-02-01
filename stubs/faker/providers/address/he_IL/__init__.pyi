from .. import Provider as AddressProvider
from _typeshed import Incomplete

class Provider(AddressProvider):
    city_formats: Incomplete
    street_name_formats: Incomplete
    street_address_formats: Incomplete
    address_formats: Incomplete
    postcode_formats: Incomplete
    street_titles: Incomplete
    city_names: Incomplete
    def city_name(self) -> str: ...
    def street_title(self) -> str: ...
