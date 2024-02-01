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
from faker.providers.phone_number.ar_AE import Provider


class Provider:
    def area_code(
        self,
    ) -> str:
        ...

    def cellphone_number(
        self,
    ) -> str:
        ...

    def cellphone_provider_code(
        self,
    ) -> str:
        ...

    def country_calling_code(
        self,
    ) -> str:
        ...

    def msisdn(
        self,
    ) -> str:
        ...

    def phone_number(
        self,
    ) -> str:
        ...

    def service_phone_number(
        self,
    ) -> str:
        ...

    def telephone_number(
        self,
    ) -> str:
        ...

    def telephone_provider_code(
        self,
    ) -> str:
        ...

    def toll_number(
        self,
    ) -> str:
        ...
