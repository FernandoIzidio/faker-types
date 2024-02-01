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

from faker.providers.user_agent import Provider


class Provider:
    def android_platform_token(
        self,
    ) -> str:
        ...

    def chrome(
        self,
        version_from: int = 13,
        version_to: int = 63,
        build_from: int = 800,
        build_to: int = 899,
    ) -> str:
        ...

    def firefox(
        self,
    ) -> str:
        ...

    def internet_explorer(
        self,
    ) -> str:
        ...

    def ios_platform_token(
        self,
    ) -> str:
        ...

    def linux_platform_token(
        self,
    ) -> str:
        ...

    def linux_processor(
        self,
    ) -> str:
        ...

    def mac_platform_token(
        self,
    ) -> str:
        ...

    def mac_processor(
        self,
    ) -> str:
        ...

    def opera(
        self,
    ) -> str:
        ...

    def safari(
        self,
    ) -> str:
        ...

    def user_agent(
        self,
    ) -> str:
        ...

    def windows_platform_token(
        self,
    ) -> str:
        ...
