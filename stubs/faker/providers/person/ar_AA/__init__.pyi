from .. import Provider as PersonProvider
from _typeshed import Incomplete
from typing import Tuple

class Provider(PersonProvider):
    formats_female: Tuple[str, ...]
    formats_male: Tuple[str, ...]
    formats: Incomplete
    first_names_female: Tuple[str, ...]
    first_names_male: Tuple[str, ...]
    first_names: Incomplete
    last_names: Tuple[str, ...]
    prefixes_female: Tuple[str, ...]
    prefixes_male: Tuple[str, ...]
