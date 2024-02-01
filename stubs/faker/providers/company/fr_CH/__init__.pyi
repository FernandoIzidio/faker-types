from ..fr_FR import Provider as CompanyProvider
from _typeshed import Incomplete

class Provider(CompanyProvider):
    company_suffixes: Incomplete
    def ide(self) -> str: ...
    uid = ide
    idi = ide
