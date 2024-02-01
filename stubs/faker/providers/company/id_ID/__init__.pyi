from .. import Provider as CompanyProvider
from _typeshed import Incomplete

class Provider(CompanyProvider):
    formats: Incomplete
    company_prefixes: Incomplete
    company_suffixes: Incomplete
    def company_prefix(self) -> str: ...
