from .. import Provider as CompanyProvider
from _typeshed import Incomplete

class Provider(CompanyProvider):
    formats: Incomplete
    catch_phrase_words: Incomplete
    bsWords: Incomplete
    company_preffixes: Incomplete
    company_suffixes: Incomplete
    def company_prefix(self) -> str: ...
