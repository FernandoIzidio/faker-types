from .. import Provider as PersonProvider
from _typeshed import Incomplete

def translate_to_bengali_digits(en_digit: str = '0') -> str: ...

class Provider(PersonProvider):
    prefixes: Incomplete
    prefixes_male: Incomplete
    prefixes_female: Incomplete
    suffixes: Incomplete
    language_names: Incomplete
    first_names_male_common: Incomplete
    first_names_male_hinduism: Incomplete
    first_names_male_islamic: Incomplete
    first_names_female_common: Incomplete
    first_names_female_hinduism: Incomplete
    first_names_female_islamic: Incomplete
    last_names_common: Incomplete
    last_names_hinduism: Incomplete
    last_names_islamic: Incomplete
    last_names_female_islamic: Incomplete
    formats_male: Incomplete
    formats_female: Incomplete
    formats: Incomplete
    first_names_male: Incomplete
    first_names_female: Incomplete
    first_names: Incomplete
    last_names_male: Incomplete
    last_names_female: Incomplete
    last_names: Incomplete
    def first_name_male_common(self) -> str: ...
    def first_name_male_hinduism(self) -> str: ...
    def first_name_male_islamic(self) -> str: ...
    def first_name_female_common(self) -> str: ...
    def first_name_female_hinduism(self) -> str: ...
    def first_name_female_islamic(self) -> str: ...
    def last_name_common(self) -> str: ...
    def last_name_hinduism(self) -> str: ...
    def last_name_islamic(self) -> str: ...
    def last_name_female_islamic(self) -> str: ...
