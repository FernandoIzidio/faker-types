from .. import Provider as GeoProvider
from decimal import Decimal

class Provider(GeoProvider):
    def local_latitude(self) -> Decimal: ...
    def local_longitude(self) -> Decimal: ...