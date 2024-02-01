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
from faker.providers.address.de import Provider


class Provider:
    def address(
        self,
    ) -> str:
        ...

    def building_number(
        self,
    ) -> str:
        ...

    def city(
        self,
    ) -> str:
        ...

    def city_suffix(
        self,
    ) -> str:
        ...

    def country(
        self,
    ) -> str:
        ...

    def country_code(self, representation: str = "alpha-2") -> str:
        ...

    def current_country(
        self,
    ) -> str:
        ...

    def current_country_code(
        self,
    ) -> str:
        ...

    def postcode(
        self,
    ) -> str:
        ...

    def street_address(
        self,
    ) -> str:
        ...

    def street_name(
        self,
    ) -> str:
        ...

    def street_suffix(
        self,
    ) -> str:
        ...
