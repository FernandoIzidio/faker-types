from .. import Provider as AutomotiveProvider
from _typeshed import Incomplete

class Provider(AutomotiveProvider):
    license_formats: Incomplete
    license_formats_motorbike: Incomplete
    license_plate_prefix_letters: str
    license_plate_prefix_letters_format_8: str
    def license_plate_motorbike(self) -> str: ...
    def license_plate_car(self) -> str: ...
    def license_plate(self) -> str: ...
