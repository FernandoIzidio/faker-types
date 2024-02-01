from .. import Provider as SsnProvider
from _typeshed import Incomplete
from typing import List

def checksum(digits: List[int]) -> int: ...

class Provider(SsnProvider):
    def ssn(self) -> str: ...
    vat_id_formats: Incomplete
    def vat_id(self) -> str: ...
