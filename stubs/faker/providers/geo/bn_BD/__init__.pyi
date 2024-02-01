from .. import Provider as GeoProvider
from _typeshed import Incomplete
from typing import Optional, Tuple

class Provider(GeoProvider):
    land_coords: Incomplete
    def local_latlng(self, country_code: str = 'BD', coords_only: bool = False) -> Optional[Tuple[str, ...]]: ...
