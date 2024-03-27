from .. import BaseProvider as BaseProvider, ElementsType as ElementsType
from ...exceptions import BaseFakerException
from _typeshed import Incomplete
from decimal import Decimal
from enum import Enum
from typing import Any, Dict, Iterable, List, Optional, Set, Tuple, Type, TypeVar, Union

TypesNames = List[str]
TypesSpec = Union[List[Type], Tuple[Type, ...]]
TEnum = TypeVar('TEnum', bound=Enum)

class EmptyEnumException(BaseFakerException): ...

class Provider(BaseProvider):
    default_value_types: ElementsType[str]
    def pyobject(self, object_type: Optional[Type[Union[bool, str, float, int, tuple, set, list, Iterable, dict]]] = None) -> Optional[Union[bool, str, float, int, tuple, set, list, Iterable, dict]]: ...
    def pybool(self, truth_probability: int = 50) -> bool: ...
    def pystr(self, min_chars: Optional[int] = None, max_chars: int = 20, prefix: str = '', suffix: str = '') -> str: ...
    def pystr_format(self, string_format: str = '?#-###{{random_int}}{{random_letter}}', letters: str = ...) -> str: ...
    def pyfloat(self, left_digits: Incomplete | None = None, right_digits: Incomplete | None = None, positive: Incomplete | None = None, min_value: Incomplete | None = None, max_value: Incomplete | None = None): ...
    def pyint(self, min_value: int = 0, max_value: int = 9999, step: int = 1) -> int: ...
    def pydecimal(self, left_digits: Optional[int] = None, right_digits: Optional[int] = None, positive: bool = False, min_value: Optional[float] = None, max_value: Optional[float] = None) -> Decimal: ...
    def pytuple(self, nb_elements: int = 10, variable_nb_elements: bool = True, value_types: Optional[TypesSpec] = None, allowed_types: Optional[TypesSpec] = None) -> Tuple[Any, ...]: ...
    def pyset(self, nb_elements: int = 10, variable_nb_elements: bool = True, value_types: Optional[TypesSpec] = None, allowed_types: Optional[TypesSpec] = None) -> Set[Any]: ...
    def pylist(self, nb_elements: int = 10, variable_nb_elements: bool = True, value_types: Optional[TypesSpec] = None, allowed_types: Optional[TypesSpec] = None) -> List[Any]: ...
    def pyiterable(self, nb_elements: int = 10, variable_nb_elements: bool = True, value_types: Incomplete | None = None, allowed_types: Incomplete | None = None): ...
    def pydict(self, nb_elements: int = 10, variable_nb_elements: bool = True, value_types: Optional[TypesSpec] = None, allowed_types: Optional[TypesSpec] = None) -> Dict[Any, Any]: ...
    def pystruct(self, count: int = 10, value_types: Optional[TypesSpec] = None, allowed_types: Optional[TypesSpec] = None) -> Tuple[List, Dict, Dict]: ...
    def enum(self, enum_cls: Type[TEnum]) -> TEnum: ...