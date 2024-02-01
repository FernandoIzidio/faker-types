from .. import Provider as SsnProvider
from _typeshed import Incomplete
from typing import List

def checksum(digits: List[int]) -> int: ...

class Provider(SsnProvider):
    scale1: Incomplete
    scale2: Incomplete
    def ssn(self, min_age: int = 16, max_age: int = 90) -> str: ...
    vat_id_formats: Incomplete
    def vat_id(self) -> str: ...
