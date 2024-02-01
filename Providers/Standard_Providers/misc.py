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

from faker.providers.misc import Provider


class Provider:
    def binary(self, length: int = 1048576) -> bytes:
        ...

    def boolean(self, chance_of_getting_true: int = 50) -> bool:
        ...

    def csv(
        self,
        header: Optional[Sequence[str]] = None,
        data_columns: Tuple[str, str] = ("{{name}}", "{{address}}"),
        num_rows: int = 10,
        include_row_ids: bool = False,
    ) -> str:
        ...

    def dsv(
        self,
        dialect: str = "faker-csv",
        header: Optional[Sequence[str]] = None,
        data_columns: Tuple[str, str] = ("{{name}}", "{{address}}"),
        num_rows: int = 10,
        include_row_ids: bool = False,
        **fmtparams
    ) -> str:
        ...

    def fixed_width(
        self,
        data_columns: Optional[list] = None,
        num_rows: int = 10,
        align: str = "left",
    ) -> str:
        ...

    def image(
        self,
        size: Tuple[int, int] = (256, 256),
        image_format: str = "png",
        hue: Union[int, Sequence[int], str, None] = None,
        luminosity: Optional[str] = None,
    ) -> bytes:
        ...

    def json(
        self,
        data_columns: Optional[List[T]] = None,
        num_rows: int = 10,
        indent: Optional[int] = None,
        cls: Optional[Type[json.encoder.JSONEncoder]] = None,
    ) -> str:
        ...

    def json_bytes(
        self,
        data_columns: Optional[List[T]] = None,
        num_rows: int = 10,
        indent: Optional[int] = None,
        cls: Optional[Type[json.encoder.JSONEncoder]] = None,
    ) -> bytes:
        ...

    def md5(self, raw_output: bool = False) -> Union[bytes, str]:
        ...

    def null_boolean(
        self,
    ) -> Optional[bool]:
        ...

    def password(
        self,
        length: int = 10,
        special_chars: bool = True,
        digits: bool = True,
        upper_case: bool = True,
        lower_case: bool = True,
    ) -> str:
        ...

    def psv(
        self,
        header: Optional[Sequence[str]] = None,
        data_columns: Tuple[str, str] = ("{{name}}", "{{address}}"),
        num_rows: int = 10,
        include_row_ids: bool = False,
    ) -> str:
        ...

    def sha1(self, raw_output: bool = False) -> Union[bytes, str]:
        ...

    def sha256(self, raw_output: bool = False) -> Union[bytes, str]:
        ...

    def tar(
        self,
        uncompressed_size: int = 65536,
        num_files: int = 1,
        min_file_size: int = 4096,
        compression: Optional[str] = None,
    ) -> bytes:
        ...

    def tsv(
        self,
        header: Optional[Sequence[str]] = None,
        data_columns: Tuple[str, str] = ("{{name}}", "{{address}}"),
        num_rows: int = 10,
        include_row_ids: bool = False,
    ) -> str:
        ...

    def uuid4(
        self,
        cast_to: Union[
            Callable[[uuid.UUID], str], Callable[[uuid.UUID], bytes], None
        ] = "str",
    ) -> Union[bytes, str, uuid.UUID]:
        ...

    def xml(
        self,
        nb_elements: int = 10,
        variable_nb_elements: bool = True,
        value_types: Union[List[Type[CT_co]], Tuple[Type[CT_co], ...], None] = None,
        allowed_types: Union[List[Type[CT_co]], Tuple[Type[CT_co], ...], None] = None,
    ) -> str:
        ...

    def zip(
        self,
        uncompressed_size: int = 65536,
        num_files: int = 1,
        min_file_size: int = 4096,
        compression: Optional[str] = None,
    ) -> bytes:
        ...
