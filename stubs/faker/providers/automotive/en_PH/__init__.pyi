from .. import Provider as AutomotiveProvider
from _typeshed import Incomplete

class Provider(AutomotiveProvider):
    protocol_licenses: Incomplete
    motorcycle_license_formats: Incomplete
    automobile_license_formats: Incomplete
    license_formats: Incomplete
    def protocol_license_plate(self) -> str: ...
    def motorcycle_license_plate(self) -> str: ...
    def automobile_license_plate(self) -> str: ...
    def license_plate(self) -> str: ...