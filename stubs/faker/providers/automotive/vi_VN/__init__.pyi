from .. import Provider as AutomotiveProvider
from _typeshed import Incomplete

class Provider(AutomotiveProvider):
    license_formats: Incomplete
    ascii_uppercase_vietnamese: str
    def license_plate(self) -> str: ...
