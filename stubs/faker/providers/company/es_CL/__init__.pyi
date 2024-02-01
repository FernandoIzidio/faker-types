from .. import Provider as CompanyProvider
from ... import ElementsType as ElementsType
from _typeshed import Incomplete

class Provider(CompanyProvider):
    formats: Incomplete
    catch_phrase_words: Incomplete
    bsWords: Incomplete
    company_prefixes: ElementsType[str]
    company_suffixes: ElementsType[str]
    def company_prefix(self) -> str: ...
