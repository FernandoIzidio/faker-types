from .. import Provider as BankProvider
from _typeshed import Incomplete

class Provider(BankProvider):
    bban_format: str
    country_code: str
    swift_bank_codes: Incomplete
    swift_location_codes: Incomplete
    swift_branch_codes: Incomplete
    banks: Incomplete
    def bank(self) -> str: ...
