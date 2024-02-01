from _typeshed import Incomplete
from faker.providers.bank import Provider as BankProvider

logger: Incomplete

class Provider(BankProvider):
    country_code: str
    bban_format: str
    swift_bank_codes: Incomplete
    swift_location_codes: Incomplete
    swift_branch_codes: Incomplete
    def bban(self) -> str: ...
    def iban(self) -> str: ...
