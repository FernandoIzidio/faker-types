from .. import BaseProvider as BaseProvider
from decimal import Decimal
from typing import Optional, Tuple, Union

localized: bool
PlaceType = Tuple[str, str, str, str, str]

class Provider(BaseProvider):
    land_coords: Tuple[PlaceType, ...]
    def coordinate(self, center: Optional[float] = None, radius: Union[float, int] = 0.001) -> Decimal: ...
    def latitude(self) -> Decimal: ...
    def longitude(self) -> Decimal: ...
    def latlng(self) -> Tuple[Decimal, Decimal]: ...
    def local_latlng(self, country_code: str = 'US', coords_only: bool = False) -> Optional[Tuple[str, ...]]: ...
    def location_on_land(self, coords_only: bool = False) -> Tuple[str, ...]: ...
