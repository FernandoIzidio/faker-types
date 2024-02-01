from ..en import Provider as AddressProvider
from _typeshed import Incomplete

class Provider(AddressProvider):
    city_prefixes: Incomplete
    city_suffixes: Incomplete
    building_number_formats: Incomplete
    street_suffixes: Incomplete
    te_reo_parts: Incomplete
    te_reo_endings: Incomplete
    postcode_formats: Incomplete
    city_formats: Incomplete
    street_name_formats: Incomplete
    street_address_formats: Incomplete
    address_formats: Incomplete
    secondary_address_formats: Incomplete
    def te_reo_part(self) -> str: ...
    def te_reo_first(self) -> str: ...
    def te_reo_ending(self) -> str: ...
    def city_prefix(self) -> str: ...
    def city_suffix(self) -> str: ...
    def rd_number(self) -> str: ...
    def secondary_address(self) -> str: ...
