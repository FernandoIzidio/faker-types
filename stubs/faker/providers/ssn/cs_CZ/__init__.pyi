from .. import Provider as BaseProvider
from typing import List, Tuple

class Provider(BaseProvider):
    vat_id_formats: Tuple[str, ...]
    national_id_months: List[str]
    def vat_id(self) -> str: ...
    def birth_number(self) -> str: ...
