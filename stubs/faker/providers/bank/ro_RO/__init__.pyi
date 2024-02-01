from _typeshed import Incomplete
from faker.providers.bank import Provider as BankProvider

class Provider(BankProvider):
    country_code: str
    bban_format: str
    swift_bank_codes: Incomplete
