from .. import Provider as PersonProvider
from _typeshed import Incomplete

class Provider(PersonProvider):
    formats: Incomplete
    first_names_male: Incomplete
    first_names_female: Incomplete
    first_names: Incomplete
    last_names: Incomplete
    romanized_formats: Incomplete
    first_romanized_names: Incomplete
    last_romanized_names: Incomplete
    def romanized_name(self) -> str: ...
    def first_romanized_name(self) -> str: ...
    def last_romanized_name(self) -> str: ...
