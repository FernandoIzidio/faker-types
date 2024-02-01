from .. import Provider as PersonProvider
from _typeshed import Incomplete

class Provider(PersonProvider):
    formats_female: Incomplete
    formats_male: Incomplete
    formats: Incomplete
    first_names_female: Incomplete
    first_names_unisex: Incomplete
    first_names_male: Incomplete
    first_names: Incomplete
    middle_names: Incomplete
    last_names: Incomplete
    prefixes_female: Incomplete
    prefixes_male: Incomplete
    def first_name_unisex(self) -> str: ...
    def middle_name(self) -> str: ...
