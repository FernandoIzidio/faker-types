from .. import Provider as AutomotiveProvider
from _typeshed import Incomplete

class Provider(AutomotiveProvider):
    license_formats: Incomplete
    def district(self) -> str: ...
    def license_plate(self) -> str: ...
