from .. import Provider as PersonProvider
from _typeshed import Incomplete
from typing import Dict, Sequence

def translit(text: str) -> str: ...

class Provider(PersonProvider):
    formats_male: Dict[str, float]
    formats_female: Dict[str, float]
    formats: Dict[str, float]
    first_names_male: Incomplete
    first_names_female: Incomplete
    first_names: Incomplete
    last_names_male: Incomplete
    last_names_female: Incomplete
    last_names: Incomplete
    middle_names_male: Incomplete
    middle_names_female: Incomplete
    middle_names: Incomplete
    language_names: Incomplete
    prefixes_male: Sequence[str]
    prefixes_female: Sequence[str]
    def middle_name(self) -> str: ...
    def middle_name_male(self) -> str: ...
    def middle_name_female(self) -> str: ...
