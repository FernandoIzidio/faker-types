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
from faker.providers.address.es import Provider


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


from faker.providers.color.es import Provider


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


from faker.providers.currency.es import Provider


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


from faker.providers.date_time.es import Provider


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


from faker.providers.job.es import Provider


class Provider:
    def job(
        self,
    ) -> str:
        ...


from faker.providers.person.es import Provider


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
