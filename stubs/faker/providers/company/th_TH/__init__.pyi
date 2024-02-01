from .. import Provider as CompanyProvider
from _typeshed import Incomplete

class Provider(CompanyProvider):
    formats: Incomplete
    company_prefixes: Incomplete
    nonprofit_prefixes: Incomplete
    company_suffixes: Incomplete
    company_limited_prefixes: Incomplete
    company_limited_suffixes: Incomplete
    def company_prefix(self) -> str: ...
    def company_limited_prefix(self) -> str: ...
    def company_limited_suffix(self) -> str: ...
    def nonprofit_prefix(self) -> str: ...
