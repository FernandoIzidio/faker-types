from .. import BaseProvider as BaseProvider, ElementsType as ElementsType
from typing import Tuple

localized: bool

class Provider(BaseProvider):
    formats: ElementsType[str]
    company_suffixes: ElementsType[str]
    catch_phrase_words: Tuple[ElementsType[str], ...]
    bsWords: Tuple[ElementsType[str], ...]
    def company(self) -> str: ...
    def company_suffix(self) -> str: ...
    def catch_phrase(self) -> str: ...
    def bs(self) -> str: ...
