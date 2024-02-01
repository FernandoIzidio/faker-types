from .. import Provider as PersonProvider
from _typeshed import Incomplete

class Provider(PersonProvider):
    formats_female: Incomplete
    formats_male: Incomplete
    formats: Incomplete
    first_names_female: Incomplete
    first_names_male: Incomplete
    first_names: Incomplete
    last_names_male: Incomplete
    last_names_female: Incomplete
    last_names_unisex: Incomplete
    last_names: Incomplete
    prefixes_female: Incomplete
    prefixes_male: Incomplete
    prefixes: Incomplete
    def last_name_male(self): ...
    def last_name_unique_to_male(self): ...
    def last_name_female(self): ...
    def last_name_unique_to_female(self): ...
    def last_name_unisex(self): ...
