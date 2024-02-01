from .. import Provider as PersonProvider
from _typeshed import Incomplete
from typing import Dict

class Provider(PersonProvider):
    formats: Incomplete
    first_names_male: Dict[str, float]
    first_names_female: Dict[str, float]
    first_names: Dict[str, float]
    last_names: Incomplete
