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
from faker.providers.address.el_GR import Provider


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

    def line_address(
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

    def street(
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

    def street_prefix_long(
        self,
    ) -> str:
        ...

    def street_prefix_short(
        self,
    ) -> str:
        ...

    def street_suffix(
        self,
    ) -> str:
        ...


from faker.providers.automotive.el_GR import Provider


class Provider:
    def license_plate(
        self,
    ) -> str:
        ...

    def vin(
        self,
    ) -> str:
        ...


from faker.providers.bank.el_GR import Provider


class Provider:
    def aba(
        self,
    ) -> str:
        ...

    def bank_country(
        self,
    ) -> str:
        ...

    def bban(
        self,
    ) -> str:
        ...

    def iban(
        self,
    ) -> str:
        ...

    def swift(
        self,
        length: Optional[int] = None,
        primary: bool = False,
        use_dataset: bool = False,
    ) -> str:
        ...

    def swift11(self, primary: bool = False, use_dataset: bool = False) -> str:
        ...

    def swift8(self, use_dataset: bool = False) -> str:
        ...


from faker.providers.color.el_GR import Provider


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


from faker.providers.company.el_GR import Provider


class Provider:
    def bs(
        self,
    ) -> str:
        ...

    def catch_phrase(
        self,
    ) -> str:
        ...

    def company(
        self,
    ) -> str:
        ...

    def company_suffix(
        self,
    ) -> str:
        ...


from faker.providers.currency.el_GR import Provider


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
    ) -> str:
        ...


from faker.providers.date_time.el_GR import Provider


class Provider:
    def am_pm(
        self,
    ) -> str:
        ...

    def century(
        self,
    ) -> str:
        ...

    def date(
        self,
        pattern: str = "%Y-%m-%d",
        end_datetime: Union[
            datetime.date, datetime.datetime, datetime.timedelta, str, int, None
        ] = None,
    ) -> str:
        ...

    def date_between(
        self,
        start_date: Union[
            datetime.date, datetime.datetime, datetime.timedelta, str, int
        ] = "-30y",
        end_date: Union[
            datetime.date, datetime.datetime, datetime.timedelta, str, int
        ] = "today",
    ) -> datetime.date:
        ...

    def date_between_dates(
        self,
        date_start: Union[
            datetime.date, datetime.datetime, datetime.timedelta, str, int, None
        ] = None,
        date_end: Union[
            datetime.date, datetime.datetime, datetime.timedelta, str, int, None
        ] = None,
    ) -> datetime.date:
        ...

    def date_object(
        self, end_datetime: Optional[datetime.datetime] = None
    ) -> datetime.date:
        ...

    def date_of_birth(
        self,
        tzinfo: Optional[datetime.tzinfo] = None,
        minimum_age: int = 0,
        maximum_age: int = 115,
    ) -> datetime.date:
        ...

    def date_this_century(
        self, before_today: bool = True, after_today: bool = False
    ) -> datetime.date:
        ...

    def date_this_decade(
        self, before_today: bool = True, after_today: bool = False
    ) -> datetime.date:
        ...

    def date_this_month(
        self, before_today: bool = True, after_today: bool = False
    ) -> datetime.date:
        ...

    def date_this_year(
        self, before_today: bool = True, after_today: bool = False
    ) -> datetime.date:
        ...

    def date_time(
        self,
        tzinfo: Optional[datetime.tzinfo] = None,
        end_datetime: Union[
            datetime.date, datetime.datetime, datetime.timedelta, str, int, None
        ] = None,
    ) -> datetime.datetime:
        ...

    def date_time_ad(
        self,
        tzinfo: Optional[datetime.tzinfo] = None,
        end_datetime: Union[
            datetime.date, datetime.datetime, datetime.timedelta, str, int, None
        ] = None,
        start_datetime: Union[
            datetime.date, datetime.datetime, datetime.timedelta, str, int, None
        ] = None,
    ) -> datetime.datetime:
        ...

    def date_time_between(
        self,
        start_date: Union[
            datetime.date, datetime.datetime, datetime.timedelta, str, int
        ] = "-30y",
        end_date: Union[
            datetime.date, datetime.datetime, datetime.timedelta, str, int
        ] = "now",
        tzinfo: Optional[datetime.tzinfo] = None,
    ) -> datetime.datetime:
        ...

    def date_time_between_dates(
        self,
        datetime_start: Union[
            datetime.date, datetime.datetime, datetime.timedelta, str, int, None
        ] = None,
        datetime_end: Union[
            datetime.date, datetime.datetime, datetime.timedelta, str, int, None
        ] = None,
        tzinfo: Optional[datetime.tzinfo] = None,
    ) -> datetime.datetime:
        ...

    def date_time_this_century(
        self,
        before_now: bool = True,
        after_now: bool = False,
        tzinfo: Optional[datetime.tzinfo] = None,
    ) -> datetime.datetime:
        ...

    def date_time_this_decade(
        self,
        before_now: bool = True,
        after_now: bool = False,
        tzinfo: Optional[datetime.tzinfo] = None,
    ) -> datetime.datetime:
        ...

    def date_time_this_month(
        self,
        before_now: bool = True,
        after_now: bool = False,
        tzinfo: Optional[datetime.tzinfo] = None,
    ) -> datetime.datetime:
        ...

    def date_time_this_year(
        self,
        before_now: bool = True,
        after_now: bool = False,
        tzinfo: Optional[datetime.tzinfo] = None,
    ) -> datetime.datetime:
        ...

    def day_of_month(
        self,
    ) -> str:
        ...

    def day_of_week(
        self,
    ):
        ...

    def future_date(
        self,
        end_date: Union[
            datetime.date, datetime.datetime, datetime.timedelta, str, int
        ] = "+30d",
        tzinfo: Optional[datetime.tzinfo] = None,
    ) -> datetime.date:
        ...

    def future_datetime(
        self,
        end_date: Union[
            datetime.date, datetime.datetime, datetime.timedelta, str, int
        ] = "+30d",
        tzinfo: Optional[datetime.tzinfo] = None,
    ) -> datetime.datetime:
        ...

    def iso8601(
        self,
        tzinfo: Optional[datetime.tzinfo] = None,
        end_datetime: Union[
            datetime.date, datetime.datetime, datetime.timedelta, str, int, None
        ] = None,
        sep: str = "T",
        timespec: str = "auto",
    ) -> str:
        ...

    def month(
        self,
    ) -> str:
        ...

    def month_name(
        self,
    ):
        ...

    def past_date(
        self,
        start_date: Union[
            datetime.date, datetime.datetime, datetime.timedelta, str, int
        ] = "-30d",
        tzinfo: Optional[datetime.tzinfo] = None,
    ) -> datetime.date:
        ...

    def past_datetime(
        self,
        start_date: Union[
            datetime.date, datetime.datetime, datetime.timedelta, str, int
        ] = "-30d",
        tzinfo: Optional[datetime.tzinfo] = None,
    ) -> datetime.datetime:
        ...

    def pytimezone(self, *args, **kwargs) -> Optional[datetime.tzinfo]:
        ...

    def time(
        self,
        pattern: str = "%H:%M:%S",
        end_datetime: Union[
            datetime.date, datetime.datetime, datetime.timedelta, str, int, None
        ] = None,
    ) -> str:
        ...

    def time_delta(
        self,
        end_datetime: Union[
            datetime.date, datetime.datetime, datetime.timedelta, str, int, None
        ] = None,
    ) -> datetime.timedelta:
        ...

    def time_object(
        self,
        end_datetime: Union[
            datetime.date, datetime.datetime, datetime.timedelta, str, int, None
        ] = None,
    ) -> datetime.time:
        ...

    def time_series(
        self,
        start_date: Union[
            datetime.date, datetime.datetime, datetime.timedelta, str, int
        ] = "-30d",
        end_date: Union[
            datetime.date, datetime.datetime, datetime.timedelta, str, int
        ] = "now",
        precision: Optional[float] = None,
        distrib: Optional[Callable[[datetime.datetime], float]] = None,
        tzinfo: Optional[datetime.tzinfo] = None,
    ) -> Iterator[Tuple[datetime.datetime, Any]]:
        ...

    def timezone(
        self,
    ) -> str:
        ...

    def unix_time(
        self,
        end_datetime: Union[
            datetime.date, datetime.datetime, datetime.timedelta, str, int, None
        ] = None,
        start_datetime: Union[
            datetime.date, datetime.datetime, datetime.timedelta, str, int, None
        ] = None,
    ) -> int:
        ...

    def year(
        self,
    ) -> str:
        ...


from faker.providers.geo.el_GR import Provider


class Provider:
    def coordinate(
        self, center: Optional[float] = None, radius: Union[float, int] = 0.001
    ) -> decimal.Decimal:
        ...

    def latitude(
        self,
    ) -> decimal.Decimal:
        ...

    def latlng(
        self,
    ) -> Tuple[decimal.Decimal, decimal.Decimal]:
        ...

    def local_latitude(
        self,
    ) -> decimal.Decimal:
        ...

    def local_latlng(self, *args, **kwargs) -> Tuple[str, str]:
        ...

    def local_longitude(
        self,
    ) -> decimal.Decimal:
        ...

    def location_on_land(self, coords_only: bool = False) -> Tuple[str, ...]:
        ...

    def longitude(
        self,
    ) -> decimal.Decimal:
        ...


from faker.providers.internet.el_GR import Provider


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


from faker.providers.job.el_GR import Provider


class Provider:
    def job(
        self,
    ) -> str:
        ...


from faker.providers.lorem.el_GR import Provider


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


from faker.providers.person.el_GR import Provider


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


from faker.providers.phone_number.el_GR import Provider


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


from faker.providers.ssn.el_GR import Provider


class Provider:
    def police_id(
        self,
    ) -> str:
        ...

    def ssn(
        self,
    ) -> str:
        ...

    def tin(
        self,
    ) -> str:
        ...

    def vat_id(self, prefix: bool = True) -> str:
        ...
