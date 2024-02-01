from ..es import Provider as AddressProvider
from _typeshed import Incomplete

class Provider(AddressProvider):
    building_number_formats: Incomplete
    street_prefixes: Incomplete
    states: Incomplete
    regions: Incomplete
    city_formats: Incomplete
    street_name_formats: Incomplete
    street_address_formats: Incomplete
    address_formats: Incomplete
    secondary_address_formats: Incomplete
    def state_name(self) -> str: ...
    def street_prefix(self) -> str: ...
    def secondary_address(self) -> str: ...
    def administrative_unit(self) -> str: ...
    state = administrative_unit
    def region(self) -> str: ...
    def postcode(self) -> str: ...
    autonomous_community = region
