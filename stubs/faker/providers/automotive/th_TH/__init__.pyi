from .. import Provider as AutomotiveProvider
from _typeshed import Incomplete

class Provider(AutomotiveProvider):
    license_formats: Incomplete
    thai_consonants: str
    def license_plate(self) -> str: ...
