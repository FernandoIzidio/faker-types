import datetime, decimal, typing_extensions, json
from typing import (
    Union,
    Optional,
    TYPE_CHECKING,
    Collection,
    Sequence,
    TypeVar,
    OrderedDict,
    List,
    Dict,
    Tuple,
    Type,
    Any,
    Iterator,
    Callable,
    Iterable,
    Set,
)

HueType = TypeVar("HueType")
T = TypeVar("T")
M = TypeVar("M")
F = TypeVar("F")
CT_co = Type("CT_co")
T_co = Type("T_co")
TEnum = Type("TeNum")
KT = TypeVar("KT")
VT = TypeVar("VT")


if TYPE_CHECKING:
    from faker.providers.credit_card import CardType

from faker.providers.geo import Provider


class Provider:
    def coordinate(
        self, center: Optional[float] = None, radius: Union[float, int] = 0.001
    ) -> decimal.Decimal:
        ...

    def latitude(
        self,
    ) -> decimal.Decimal:
        ...

    def latlng(
        self,
    ) -> Tuple[decimal.Decimal, decimal.Decimal]:
        ...

    def local_latlng(
        self, country_code: str = "US", coords_only: bool = False
    ) -> Optional[Tuple[str, ...]]:
        ...

    def location_on_land(self, coords_only: bool = False) -> Tuple[str, ...]:
        ...

    def longitude(
        self,
    ) -> decimal.Decimal:
        ...
