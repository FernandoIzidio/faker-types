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

from faker.providers.file import Provider


class Provider:
    def file_extension(self, category: Optional[str] = None) -> str:
        ...

    def file_name(
        self, category: Optional[str] = None, extension: Optional[str] = None
    ) -> str:
        ...

    def file_path(
        self,
        depth: int = 1,
        category: Optional[str] = None,
        extension: Optional[str] = None,
        absolute: Optional[bool] = True,
    ) -> str:
        ...

    def mime_type(self, category: Optional[str] = None) -> str:
        ...

    def unix_device(self, prefix: Optional[str] = None) -> str:
        ...

    def unix_partition(self, prefix: Optional[str] = None) -> str:
        ...
