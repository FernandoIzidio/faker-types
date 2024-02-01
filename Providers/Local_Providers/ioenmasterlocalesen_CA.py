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
from faker.providers.address.en_CA import Provider


class Provider:
    def address(
        self,
    ) -> str:
        ...

    def administrative_unit(
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

    def city_prefix(
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

    def postal_code_letter(
        self,
    ) -> str:
        ...

    def postalcode(
        self,
    ) -> str:
        ...

    def postalcode_in_province(self, province_abbr: Optional[str] = None) -> str:
        ...

    def postcode(
        self,
    ) -> str:
        ...

    def postcode_in_province(self, province_abbr: Optional[str] = None) -> str:
        ...

    def province(
        self,
    ) -> str:
        ...

    def province_abbr(
        self,
    ) -> str:
        ...

    def secondary_address(
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


from faker.providers.automotive.en_CA import Provider


class Provider:
    def license_plate(
        self,
    ) -> str:
        ...

    def vin(
        self,
    ) -> str:
        ...


from faker.providers.barcode.en_CA import Provider


class Provider:
    def ean(
        self,
        length: int = 13,
        prefixes: Tuple[Union[int, str, Tuple[Union[int, str], ...]], ...] = (),
    ) -> str:
        ...

    def ean13(
        self,
        prefixes: Tuple[Union[int, str, Tuple[Union[int, str], ...]], ...] = (),
        leading_zero: Optional[bool] = None,
    ) -> str:
        ...

    def ean8(self, prefixes: Tuple[()] = ()) -> str:
        ...

    def localized_ean(self, length: int = 13) -> str:
        ...

    def localized_ean13(
        self,
    ) -> str:
        ...

    def localized_ean8(
        self,
    ) -> str:
        ...

    def upc_a(
        self,
        upc_ae_mode: bool = False,
        base: Optional[str] = None,
        number_system_digit: Optional[int] = None,
    ) -> str:
        ...

    def upc_e(
        self,
        base: Optional[str] = None,
        number_system_digit: Optional[int] = None,
        safe_mode: bool = True,
    ) -> str:
        ...


from faker.providers.currency.en_CA import Provider


class Provider:
    def cryptocurrency(
        self,
    ) -> Tuple[str, str]:
        ...

    def cryptocurrency_code(
        self,
    ) -> str:
        ...

    def cryptocurrency_name(
        self,
    ) -> str:
        ...

    def currency(
        self,
    ) -> Tuple[str, str]:
        ...

    def currency_code(
        self,
    ) -> str:
        ...

    def currency_name(
        self,
    ) -> str:
        ...

    def currency_symbol(self, code: Optional[str] = None) -> str:
        ...

    def pricetag(
        self,
    ):
        ...


from faker.providers.phone_number.en_CA import Provider


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


from faker.providers.ssn.en_CA import Provider


class Provider:
    def ssn(
        self,
    ) -> str:
        ...
