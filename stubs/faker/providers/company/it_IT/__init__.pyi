from .. import Provider as CompanyProvider
from _typeshed import Incomplete
from faker.utils.checksums import calculate_luhn as calculate_luhn

class Provider(CompanyProvider):
    formats: Incomplete
    catch_phrase_words: Incomplete
    bsWords: Incomplete
    company_suffixes: Incomplete
    def company_vat(self) -> str: ...
