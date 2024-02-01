from ..es import Provider as PersonProvider
from _typeshed import Incomplete
from typing import Tuple

class Provider(PersonProvider):
    formats_male: Tuple[str, ...]
    formats_female: Tuple[str, ...]
    formats: Tuple[str, ...]
    first_names_male: Tuple[str, ...]
    first_names_female: Tuple[str, ...]
    first_names: Incomplete
    last_names: Incomplete
    prefixes: Incomplete
