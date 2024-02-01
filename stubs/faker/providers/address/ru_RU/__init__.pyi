from .. import Provider as AddressProvider
from _typeshed import Incomplete

class Provider(AddressProvider):
    city_suffixes: Incomplete
    street_suffixes: Incomplete
    region_suffixes: Incomplete
    city_formats: Incomplete
    street_address_formats: Incomplete
    address_formats: Incomplete
    postcode_formats: Incomplete
    building_number_formats: Incomplete
    city_prefixes: Incomplete
    street_suffixes_masc: Incomplete
    street_suffixes_fem: Incomplete
    street_suffixes_neu: Incomplete
    street_titles: Incomplete
    street_titles_noflex: Incomplete
    street_titles_irregular_masc: Incomplete
    street_titles_irregular_neu: Incomplete
    city_names: Incomplete
    region_republics: Incomplete
    region_krai: Incomplete
    region_oblast: Incomplete
    region_ao: Incomplete
    countries: Incomplete
    def city_prefix(self) -> str: ...
    def city_name(self) -> str: ...
    def country(self) -> str: ...
    def administrative_unit(self) -> str: ...
    region = administrative_unit
    def street_suffix(self) -> str: ...
    def street_title(self) -> str: ...
    def street_name(self) -> str: ...
