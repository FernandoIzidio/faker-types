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

from faker.providers.barcode import Provider


class Provider:
    def ean(
        self,
        length: int = 13,
        prefixes: Tuple[Union[int, str, Tuple[Union[int, str], ...]], ...] = (),
    ) -> str:
        ...

    def ean13(
        self, prefixes: Tuple[Union[int, str, Tuple[Union[int, str], ...]], ...] = ()
    ) -> str:
        ...

    def ean8(self, prefixes: Tuple[()] = ()) -> str:
        ...

    def localized_ean(self, length: int = 13) -> str:
        ...

    def localized_ean13(
        self,
    ) -> str:
        ...

    def localized_ean8(
        self,
    ) -> str:
        ...
