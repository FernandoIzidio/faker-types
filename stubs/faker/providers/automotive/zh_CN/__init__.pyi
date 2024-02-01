from .. import Provider as AutomotiveProvider
from _typeshed import Incomplete

class Provider(AutomotiveProvider):
    province_code: Incomplete
    def license_plate(self) -> str: ...
