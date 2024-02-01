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

from faker.providers.credit_card import Provider


class Provider:
    def credit_card_expire(
        self,
        start: Union[
            datetime.date, datetime.datetime, datetime.timedelta, str, int
        ] = "now",
        end: Union[
            datetime.date, datetime.datetime, datetime.timedelta, str, int
        ] = "+10y",
        date_format: str = "%m/%y",
    ) -> str:
        ...

    def credit_card_full(self, card_type: Optional[CardType] = None) -> str:
        ...

    def credit_card_number(self, card_type: Optional[CardType] = None) -> str:
        ...

    def credit_card_provider(self, card_type: Optional[CardType] = None) -> str:
        ...

    def credit_card_security_code(self, card_type: Optional[CardType] = None) -> str:
        ...
