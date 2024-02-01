from .. import Provider as CompanyProvider
from _typeshed import Incomplete
from faker.utils.checksums import calculate_luhn as calculate_luhn
from typing import Tuple

class Provider(CompanyProvider):
    formats: Incomplete
    catch_phrase_formats: Incomplete
    nouns: Incomplete
    verbs: Incomplete
    attributes: Incomplete
    company_suffixes: Tuple[str, ...]
    siren_format: str
    def catch_phrase_noun(self) -> str: ...
    def catch_phrase_attribute(self) -> str: ...
    def catch_phrase_verb(self) -> str: ...
    def catch_phrase(self) -> str: ...
    words_which_should_not_appear_twice: Incomplete
    def siren(self) -> str: ...
    def siret(self, max_sequential_digits: int = 2) -> str: ...
