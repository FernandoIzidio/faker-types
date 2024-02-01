from .. import Provider as CompanyProvider
from _typeshed import Incomplete

class Provider(CompanyProvider):
    company_names: Incomplete
    def company(self) -> str: ...
