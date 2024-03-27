from .. import Provider as AddressProvider
from _typeshed import Incomplete
from typing import Tuple

class Provider(AddressProvider):
    city_suffixes: Incomplete
    street_prefixes: Incomplete
    city_formats: Incomplete
    street_name_formats: Incomplete
    street_address_formats: Incomplete
    address_formats: Incomplete
    building_number_formats: Incomplete
    postcode_raw_formats: Incomplete
    postcode_all_formats: Incomplete
    bairros: Incomplete
    countries: Incomplete
    estados: Incomplete
    def street_prefix(self) -> str: ...
    def estado(self) -> Tuple[str, str]: ...
    def estado_nome(self) -> str: ...
    def estado_sigla(self) -> str: ...
    def bairro(self) -> str: ...
    def postcode(self, formatted: bool = True) -> str: ...
    def neighborhood(self) -> str: ...
    def administrative_unit(self) -> str: ...
    state = administrative_unit
    def state_abbr(self) -> str: ...