from .. import Provider as CompanyProvider
from _typeshed import Incomplete

class Provider(CompanyProvider):
    formats: Incomplete
    company_suffixes: Incomplete
    def company_business_id(self) -> str: ...
    def company_vat(self) -> str: ...
