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

from faker.providers.python import Provider


class Provider:
    def enum(self, enum_cls: Type[TEnum]) -> TEnum:
        ...

    def pybool(self, truth_probability: int = 50) -> bool:
        ...

    def pydecimal(
        self,
        left_digits=None,
        right_digits=None,
        positive=False,
        min_value=None,
        max_value=None,
    ):
        ...

    def pydict(
        self,
        nb_elements: int = 10,
        variable_nb_elements: bool = True,
        value_types: Union[List[Type[CT_co]], Tuple[Type[CT_co], ...], None] = None,
        allowed_types: Union[List[Type[CT_co]], Tuple[Type[CT_co], ...], None] = None,
    ) -> Dict[Any, Any]:
        ...

    def pyfloat(
        self,
        left_digits=None,
        right_digits=None,
        positive=False,
        min_value=None,
        max_value=None,
    ):
        ...

    def pyint(self, min_value: int = 0, max_value: int = 9999, step: int = 1) -> int:
        ...

    def pyiterable(
        self,
        nb_elements: int = 10,
        variable_nb_elements: bool = True,
        value_types: Union[List[Type[CT_co]], Tuple[Type[CT_co], ...], None] = None,
        allowed_types: Union[List[Type[CT_co]], Tuple[Type[CT_co], ...], None] = None,
    ) -> Iterable[Any]:
        ...

    def pylist(
        self,
        nb_elements: int = 10,
        variable_nb_elements: bool = True,
        value_types: Union[List[Type[CT_co]], Tuple[Type[CT_co], ...], None] = None,
        allowed_types: Union[List[Type[CT_co]], Tuple[Type[CT_co], ...], None] = None,
    ) -> List[Any]:
        ...

    def pyobject(
        self,
        object_type: Optional[
            Type[Union[bool, str, float, int, tuple, set, list, Iterable[T_co], dict]]
        ] = None,
    ) -> Union[bool, str, float, int, tuple, set, list, Iterable[T_co], dict, None]:
        ...

    def pyset(
        self,
        nb_elements: int = 10,
        variable_nb_elements: bool = True,
        value_types: Union[List[Type[CT_co]], Tuple[Type[CT_co], ...], None] = None,
        allowed_types: Union[List[Type[CT_co]], Tuple[Type[CT_co], ...], None] = None,
    ) -> Set[Any]:
        ...

    def pystr(
        self,
        min_chars: Optional[int] = None,
        max_chars: int = 20,
        prefix: str = "",
        suffix: str = "",
    ) -> str:
        ...

    def pystr_format(
        self,
        string_format: str = "?#-###{{random_int}}{{random_letter}}",
        letters: str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
    ) -> str:
        ...

    def pystruct(
        self,
        count: int = 10,
        value_types: Union[List[Type[CT_co]], Tuple[Type[CT_co], ...], None] = None,
        allowed_types: Union[List[Type[CT_co]], Tuple[Type[CT_co], ...], None] = None,
    ) -> Tuple[List[T], Dict[KT, VT], Dict[KT, VT]]:
        ...

    def pytuple(
        self,
        nb_elements: int = 10,
        variable_nb_elements: bool = True,
        value_types: Union[List[Type[CT_co]], Tuple[Type[CT_co], ...], None] = None,
        allowed_types: Union[List[Type[CT_co]], Tuple[Type[CT_co], ...], None] = None,
    ) -> Tuple[Any, ...]:
        ...
