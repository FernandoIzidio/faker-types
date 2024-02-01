from .. import Provider as SsnProvider
from ....typing import SexLiteral as SexLiteral
from _typeshed import Incomplete
from typing import List, Optional, Sequence

def checksum(digits: Sequence[int], scale: List[int]) -> int: ...

class Provider(SsnProvider):
    scale1: Incomplete
    scale2: Incomplete
    def ssn(self, dob: Optional[str] = None, gender: Optional[SexLiteral] = None) -> str: ...
