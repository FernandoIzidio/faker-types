from ..es import Provider as PersonProvider
from _typeshed import Incomplete
from typing import Dict

class Provider(PersonProvider):
    formats_male: Incomplete
    formats_female: Incomplete
    formats: Incomplete
    first_names_male: Dict[str, float]
    first_names_female: Dict[str, float]
    @property
    def first_names(self): ...
    last_names: Incomplete
    prefixes_male: Incomplete
    prefixes_female: Incomplete
    def name(self) -> str: ...
    def given_name(self) -> str: ...
    def given_name_male(self) -> str: ...
    def given_name_female(self) -> str: ...
