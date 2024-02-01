from .. import Provider as SsnProvider
from ....typing import SexLiteral as SexLiteral
from _typeshed import Incomplete
from typing import Optional

def zfix(d: int) -> str: ...

class Provider(SsnProvider):
    def ssn(self, dob: Optional[str] = None, gender: Optional[SexLiteral] = None) -> str: ...
    vat_id_formats: Incomplete
    def vat_id(self) -> str: ...
