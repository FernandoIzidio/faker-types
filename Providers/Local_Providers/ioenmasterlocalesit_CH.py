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
import uuid

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
from faker.providers.bank.it_CH import Provider


class Provider:
    def aba(
        self,
    ) -> str:
        ...

    def bank_country(
        self,
    ) -> str:
        ...

    def bban(
        self,
    ) -> str:
        ...

    def iban(
        self,
    ) -> str:
        ...

    def swift(
        self,
        length: Optional[int] = None,
        primary: bool = False,
        use_dataset: bool = False,
    ) -> str:
        ...

    def swift11(self, primary: bool = False, use_dataset: bool = False) -> str:
        ...

    def swift8(self, use_dataset: bool = False) -> str:
        ...
