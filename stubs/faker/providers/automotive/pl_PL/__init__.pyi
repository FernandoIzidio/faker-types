from .. import Provider as AutomotiveProvider
from _typeshed import Incomplete
from typing import List

class Provider(AutomotiveProvider):
    license_formats: Incomplete
    def license_plate_regex_formats(self) -> List[str]: ...
