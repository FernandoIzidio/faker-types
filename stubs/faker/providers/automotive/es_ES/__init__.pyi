from .. import Provider as AutomotiveProvider
from _typeshed import Incomplete
from typing import Optional

class Provider(AutomotiveProvider):
    license_formats: Incomplete
    license_plate_new_format_suffix_letters: str
    license_plate_old_format_suffix_letters: str
    province_prefix: Incomplete
    def license_plate_unified(self) -> str: ...
    def license_plate_by_province(self, province_prefix: Optional[str] = None) -> str: ...
    def license_plate(self) -> str: ...
