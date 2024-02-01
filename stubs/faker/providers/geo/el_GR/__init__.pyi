from .. import Provider as GeoProvider
from _typeshed import Incomplete
from decimal import Decimal
from typing import Any, Tuple

class Provider(GeoProvider):
    poly: Incomplete
    def local_latlng(self, *args: Any, **kwargs: Any) -> Tuple[str, str]: ...
    def local_latitude(self) -> Decimal: ...
    def local_longitude(self) -> Decimal: ...
