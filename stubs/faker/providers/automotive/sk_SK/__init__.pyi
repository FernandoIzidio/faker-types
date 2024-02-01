from .. import Provider as AutomotiveProvider
from _typeshed import Incomplete

class Provider(AutomotiveProvider):
    license_plate_prefix: Incomplete
    license_plate_suffix: Incomplete
    def license_plate(self) -> str: ...
