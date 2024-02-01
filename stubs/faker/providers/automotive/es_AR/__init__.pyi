from .. import Provider as AutomotiveProvider
from _typeshed import Incomplete

class Provider(AutomotiveProvider):
    license_plate_old_format_first_letter: Incomplete
    license_plate_new_first_letter: Incomplete
    license_plate_new_second_letter: Incomplete
    license_formats: Incomplete
    def license_plate_old(self) -> str: ...
    def license_plate_mercosur(self) -> str: ...
    def license_plate(self) -> str: ...
