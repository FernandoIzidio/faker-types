from .. import Provider as BaseProvider
from _typeshed import Incomplete

def calculate_checksum(ssn_without_checksum: int) -> int: ...

class Provider(BaseProvider):
    vat_id_formats: Incomplete
    departments_and_municipalities: Incomplete
    def ssn(self) -> str: ...
    def vat_id(self) -> str: ...
