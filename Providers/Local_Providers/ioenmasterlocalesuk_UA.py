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
from faker.providers.address.uk_UA import Provider


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

    def postcode(
        self,
    ) -> str:
        ...

    def region(
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

    def street_prefix(
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


from faker.providers.color.uk_UA import Provider


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


from faker.providers.internet.uk_UA import Provider


class Provider:
    def ascii_company_email(
        self,
    ) -> str:
        ...

    def ascii_email(
        self,
    ) -> str:
        ...

    def ascii_free_email(
        self,
    ) -> str:
        ...

    def ascii_safe_email(
        self,
    ) -> str:
        ...

    def company_email(
        self,
    ) -> str:
        ...

    def dga(
        self,
        year: Optional[int] = None,
        month: Optional[int] = None,
        day: Optional[int] = None,
        tld: Optional[str] = None,
        length: Optional[int] = None,
    ) -> str:
        ...

    def domain_name(self, levels: int = 1) -> str:
        ...

    def domain_word(
        self,
    ) -> str:
        ...

    def email(self, safe: bool = True, domain: Optional[str] = None) -> str:
        ...

    def free_email(
        self,
    ) -> str:
        ...

    def free_email_domain(
        self,
    ) -> str:
        ...

    def hostname(self, levels: int = 1) -> str:
        ...

    def http_method(
        self,
    ) -> str:
        ...

    def iana_id(
        self,
    ) -> str:
        ...

    def image_url(
        self,
        width: Optional[int] = None,
        height: Optional[int] = None,
        placeholder_url: Optional[str] = None,
    ) -> str:
        ...

    def ipv4(
        self,
        network: bool = False,
        address_class: Optional[str] = None,
        private: Optional[str] = None,
    ) -> str:
        ...

    def ipv4_network_class(
        self,
    ) -> str:
        ...

    def ipv4_private(
        self, network: bool = False, address_class: Optional[str] = None
    ) -> str:
        ...

    def ipv4_public(
        self, network: bool = False, address_class: Optional[str] = None
    ) -> str:
        ...

    def ipv6(self, network: bool = False) -> str:
        ...

    def mac_address(
        self,
    ) -> str:
        ...

    def nic_handle(self, suffix: str = "FAKE") -> str:
        ...

    def nic_handles(self, count: int = 1, suffix: str = "????") -> List[str]:
        ...

    def port_number(
        self, is_system: bool = False, is_user: bool = False, is_dynamic: bool = False
    ) -> int:
        ...

    def ripe_id(
        self,
    ) -> str:
        ...

    def safe_domain_name(
        self,
    ) -> str:
        ...

    def safe_email(
        self,
    ) -> str:
        ...

    def slug(self, value: Optional[str] = None) -> str:
        ...

    def tld(
        self,
    ) -> str:
        ...

    def uri(
        self,
    ) -> str:
        ...

    def uri_extension(
        self,
    ) -> str:
        ...

    def uri_page(
        self,
    ) -> str:
        ...

    def uri_path(self, deep: Optional[int] = None) -> str:
        ...

    def url(self, schemes: Optional[List[str]] = None) -> str:
        ...

    def user_name(
        self,
    ) -> str:
        ...


from faker.providers.job.uk_UA import Provider


class Provider:
    def job(
        self,
    ) -> str:
        ...


from faker.providers.person.uk_UA import Provider


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


from faker.providers.phone_number.uk_UA import Provider


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


from faker.providers.ssn.uk_UA import Provider


class Provider:
    def ssn(
        self,
    ) -> str:
        ...
