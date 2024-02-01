from .. import Provider as BaseProvider
from typing import Tuple

class Provider(BaseProvider):
    nino_formats: Tuple[str, ...]
    def ssn(self) -> str: ...
    vat_id_formats: Tuple[str, ...]
    def vat_id(self) -> str: ...
