from .. import Provider as CompanyProvider
from _typeshed import Incomplete

class Provider(CompanyProvider):
    formats: Incomplete
    company_prefixes: Incomplete
    company_categories: Incomplete
    def company_prefix(self) -> str: ...
    def company_category(self) -> str: ...
