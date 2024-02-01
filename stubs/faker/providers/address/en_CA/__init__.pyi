from ..en import Provider as AddressProvider
from _typeshed import Incomplete
from faker.providers import ElementsType as ElementsType
from typing import Optional

class Provider(AddressProvider):
    postal_code_letters: Incomplete
    city_prefixes: ElementsType[str]
    city_suffixes: ElementsType[str]
    building_number_formats: Incomplete
    street_suffixes: Incomplete
    postal_code_formats: Incomplete
    provinces: Incomplete
    provinces_abbr: Incomplete
    provinces_postcode_prefixes: Incomplete
    city_formats: ElementsType[str]
    street_name_formats: Incomplete
    street_address_formats: Incomplete
    address_formats: Incomplete
    secondary_address_formats: Incomplete
    def administrative_unit(self) -> str: ...
    province = administrative_unit
    def province_abbr(self) -> str: ...
    def city_prefix(self) -> str: ...
    def secondary_address(self) -> str: ...
    def postal_code_letter(self) -> str: ...
    def postcode(self) -> str: ...
    def postcode_in_province(self, province_abbr: Optional[str] = None) -> str: ...
    def postalcode_in_province(self, province_abbr: Optional[str] = None) -> str: ...
    def postalcode(self) -> str: ...
