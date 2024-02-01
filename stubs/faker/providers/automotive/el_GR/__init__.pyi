from .. import Provider as AutomotiveProvider
from _typeshed import Incomplete

class Provider(AutomotiveProvider):
    uppercase_letters: str
    license_formats: Incomplete
    def license_plate(self) -> str: ...
