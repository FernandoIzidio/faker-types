from .. import Provider as BaseProvider
from faker.utils.checksums import calculate_luhn as calculate_luhn

def tin_checksum(tin: str) -> int: ...

class Provider(BaseProvider):
    police_id_format: str
    def vat_id(self, prefix: bool = True) -> str: ...
    def tin(self) -> str: ...
    def ssn(self) -> str: ...
    def police_id(self) -> str: ...