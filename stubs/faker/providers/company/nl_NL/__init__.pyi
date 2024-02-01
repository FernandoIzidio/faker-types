from .. import Provider as CompanyProvider
from _typeshed import Incomplete

class Provider(CompanyProvider):
    formats: Incomplete
    company_prefixes: Incomplete
    company_suffixes: Incomplete
    large_companies: Incomplete
    def large_company(self) -> str: ...
    def company_prefix(self) -> str: ...
