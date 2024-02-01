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
from faker.providers.address.he_IL import Provider


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

    def city_name(
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

    def street_title(
        self,
    ) -> str:
        ...


from faker.providers.automotive.he_IL import Provider


class Provider:
    def license_plate(
        self,
    ) -> str:
        ...

    def vin(
        self,
    ) -> str:
        ...


from faker.providers.color.he_IL import Provider


class Provider:
    def color(
        self,
        hue: Optional[HueType] = None,
        luminosity: Optional[str] = None,
        color_format: str = "hex",
    ) -> str:
        ...

    def color_name(
        self,
    ) -> str:
        ...

    def hex_color(
        self,
    ) -> str:
        ...

    def rgb_color(
        self,
    ) -> str:
        ...

    def rgb_css_color(
        self,
    ) -> str:
        ...

    def safe_color_name(
        self,
    ) -> str:
        ...

    def safe_hex_color(
        self,
    ) -> str:
        ...


from faker.providers.lorem.he_IL import Provider


class Provider:
    def paragraph(
        self,
        nb_sentences: int = 3,
        variable_nb_sentences: bool = True,
        ext_word_list: Optional[Sequence[str]] = None,
    ) -> str:
        ...

    def paragraphs(
        self, nb: int = 3, ext_word_list: Optional[Sequence[str]] = None
    ) -> List[str]:
        ...

    def sentence(
        self,
        nb_words: int = 6,
        variable_nb_words: bool = True,
        ext_word_list: Optional[Sequence[str]] = None,
    ) -> str:
        ...

    def sentences(
        self, nb: int = 3, ext_word_list: Optional[Sequence[str]] = None
    ) -> List[str]:
        ...

    def text(
        self, max_nb_chars: int = 200, ext_word_list: Optional[Sequence[str]] = None
    ) -> str:
        ...

    def texts(
        self,
        nb_texts: int = 3,
        max_nb_chars: int = 200,
        ext_word_list: Optional[Sequence[str]] = None,
    ) -> List[str]:
        ...

    def word(
        self,
        part_of_speech: Optional[str] = None,
        ext_word_list: Optional[Sequence[str]] = None,
    ) -> str:
        ...

    def words(
        self,
        nb: int = 3,
        part_of_speech: Optional[str] = None,
        ext_word_list: Optional[Sequence[str]] = None,
        unique: bool = False,
    ) -> List[str]:
        ...


from faker.providers.person.he_IL import Provider


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


from faker.providers.phone_number.he_IL import Provider


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


from faker.providers.ssn.he_IL import Provider


class Provider:
    def ssn(
        self,
    ) -> str:
        ...
