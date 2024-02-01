from .. import Provider as BankProvider
from _typeshed import Incomplete

class Provider(BankProvider):
    country_code: str
    region_codes: Incomplete
    department_code_formats: Incomplete
    credit_organization_code_formats: Incomplete
    checking_account_codes: Incomplete
    organization_codes: Incomplete
    currency_codes: Incomplete
    banks: Incomplete
    def bic(self) -> str: ...
    def correspondent_account(self) -> str: ...
    def checking_account(self) -> str: ...
    def bank(self) -> str: ...
