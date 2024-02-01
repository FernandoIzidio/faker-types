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

from faker.providers.profile import Provider


class Provider:
    def profile(
        self,
        fields: Optional[List[str]] = None,
        sex: Optional[typing_extensions.Literal["M", "F"][M, F]] = None,
    ) -> Dict[
        str,
        Union[str, Tuple[decimal.Decimal, decimal.Decimal], List[str], datetime.date],
    ]:
        ...

    def simple_profile(
        self, sex: Optional[typing_extensions.Literal["M", "F"][M, F]] = None
    ) -> Dict[
        str, Union[str, datetime.date, typing_extensions.Literal["M", "F"][M, F]]
    ]:
        ...
