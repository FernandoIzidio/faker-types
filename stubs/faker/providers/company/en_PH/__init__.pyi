from .. import Provider as CompanyProvider
from _typeshed import Incomplete

class Provider(CompanyProvider):
    formats: Incomplete
    company_suffixes: Incomplete
    company_types: Incomplete
    company_products: Incomplete
    company_nouns: Incomplete
    company_adjectives: Incomplete
    def company_type(self) -> str: ...
    def random_company_adjective(self) -> str: ...
    def random_company_noun_chain(self) -> str: ...
    def random_company_product(self) -> str: ...
    def random_company_acronym(self) -> str: ...