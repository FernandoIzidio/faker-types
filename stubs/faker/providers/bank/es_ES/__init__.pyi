from .. import Provider as BankProvider

class Provider(BankProvider):
    bban_format: str
    country_code: str
