from .. import Provider as AutomotiveProvider
from _typeshed import Incomplete

class Provider(AutomotiveProvider):
    LICENSE_FORMAT_EN: str
    LICENSE_FORMAT_AR: str
    PLATE_CHARS_EN: str
    PLATE_CHARS_AR: str
    PLATE_MAP: Incomplete
    def license_plate_en(self) -> str: ...
    def license_plate_ar(self) -> str: ...
    def license_plate(self, ar: bool = True) -> str: ...
