from .. import Provider as SsnProvider
from ....typing import SexLiteral as SexLiteral
from typing import List, Optional

class Provider(SsnProvider):
    area_codes: List[str]
    def ssn(self, min_age: int = 18, max_age: int = 90, gender: Optional[SexLiteral] = None, area_code: str = '') -> str: ...
