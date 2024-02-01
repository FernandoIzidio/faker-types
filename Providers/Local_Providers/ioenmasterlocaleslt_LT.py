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
from faker.providers.automotive.lt_LT import Provider


class Provider:
    def license_plate(
        self,
    ) -> str:
        ...

    def vin(
        self,
    ) -> str:
        ...


from faker.providers.person.lt_LT import Provider


class Provider:
    def first_name(
        self,
    ) -> str:
        ...

    def first_name_female(
        self,
    ) -> str:
        ...

    def first_name_male(
        self,
    ) -> str:
        ...

    def first_name_nonbinary(
        self,
    ) -> str:
        ...

    def language_name(
        self,
    ) -> str:
        ...

    def last_name(
        self,
    ) -> str:
        ...

    def last_name_female(
        self,
    ) -> str:
        ...

    def last_name_male(
        self,
    ) -> str:
        ...

    def last_name_nonbinary(
        self,
    ) -> str:
        ...

    def name(
        self,
    ) -> str:
        ...

    def name_female(
        self,
    ) -> str:
        ...

    def name_male(
        self,
    ) -> str:
        ...

    def name_nonbinary(
        self,
    ) -> str:
        ...

    def prefix(
        self,
    ) -> str:
        ...

    def prefix_female(
        self,
    ) -> str:
        ...

    def prefix_male(
        self,
    ) -> str:
        ...

    def prefix_nonbinary(
        self,
    ) -> str:
        ...

    def suffix(
        self,
    ) -> str:
        ...

    def suffix_female(
        self,
    ) -> str:
        ...

    def suffix_male(
        self,
    ) -> str:
        ...

    def suffix_nonbinary(
        self,
    ) -> str:
        ...


from faker.providers.phone_number.lt_LT import Provider


class Provider:
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


from faker.providers.ssn.lt_LT import Provider


class Provider:
    def ssn(
        self,
    ) -> str:
        ...

    def vat_id(
        self,
    ) -> str:
        ...
