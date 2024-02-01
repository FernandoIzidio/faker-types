from .. import Provider as PersonProvider
from _typeshed import Incomplete
from typing import Dict

class Provider(PersonProvider):
    formats_male: Dict[str, float]
    formats_female: Dict[str, float]
    formats: Dict[str, float]
    last_names: Incomplete
    first_names_male: Dict[str, float]
    first_names_female: Dict[str, float]
    first_names: Dict[str, float]
    prefixes: Dict[str, float]
    def first_name_male_abbreviated(self) -> str: ...
    def first_name_female_abbreviated(self) -> str: ...
