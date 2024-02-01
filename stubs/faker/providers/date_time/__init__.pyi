from .. import BaseProvider as BaseProvider, ElementsType as ElementsType
from _typeshed import Incomplete
from datetime import date as dtdate, datetime, time as dttime, timedelta, tzinfo as TzInfo
from faker.typing import Country as Country, DateParseType as DateParseType
from typing import Any, Callable, Iterator, Optional, Tuple, Union

localized: bool

def datetime_to_timestamp(dt: Union[dtdate, datetime]) -> int: ...
def timestamp_to_datetime(timestamp: Union[int, float], tzinfo: Optional[TzInfo]) -> datetime: ...
def change_year(current_date: dtdate, year_diff: int) -> dtdate: ...

class ParseError(ValueError): ...

timedelta_pattern: str

class Provider(BaseProvider):
    centuries: ElementsType[str]
    countries: Incomplete
    regex: Incomplete
    def unix_time(self, end_datetime: Optional[DateParseType] = None, start_datetime: Optional[DateParseType] = None) -> float: ...
    def time_delta(self, end_datetime: Optional[DateParseType] = None) -> timedelta: ...
    def date_time(self, tzinfo: Optional[TzInfo] = None, end_datetime: Optional[DateParseType] = None) -> datetime: ...
    def date_time_ad(self, tzinfo: Optional[TzInfo] = None, end_datetime: Optional[DateParseType] = None, start_datetime: Optional[DateParseType] = None) -> datetime: ...
    def iso8601(self, tzinfo: Optional[TzInfo] = None, end_datetime: Optional[DateParseType] = None, sep: str = 'T', timespec: str = 'auto') -> str: ...
    def date(self, pattern: str = '%Y-%m-%d', end_datetime: Optional[DateParseType] = None) -> str: ...
    def date_object(self, end_datetime: Optional[datetime] = None) -> dtdate: ...
    def time(self, pattern: str = '%H:%M:%S', end_datetime: Optional[DateParseType] = None) -> str: ...
    def time_object(self, end_datetime: Optional[DateParseType] = None) -> dttime: ...
    def date_time_between(self, start_date: DateParseType = '-30y', end_date: DateParseType = 'now', tzinfo: Optional[TzInfo] = None) -> datetime: ...
    def date_between(self, start_date: DateParseType = '-30y', end_date: DateParseType = 'today') -> dtdate: ...
    def future_datetime(self, end_date: DateParseType = '+30d', tzinfo: Optional[TzInfo] = None) -> datetime: ...
    def future_date(self, end_date: DateParseType = '+30d', tzinfo: Optional[TzInfo] = None) -> dtdate: ...
    def past_datetime(self, start_date: DateParseType = '-30d', tzinfo: Optional[TzInfo] = None) -> datetime: ...
    def past_date(self, start_date: DateParseType = '-30d', tzinfo: Optional[TzInfo] = None) -> dtdate: ...
    def date_time_between_dates(self, datetime_start: Optional[DateParseType] = None, datetime_end: Optional[DateParseType] = None, tzinfo: Optional[TzInfo] = None) -> datetime: ...
    def date_between_dates(self, date_start: Optional[DateParseType] = None, date_end: Optional[DateParseType] = None) -> dtdate: ...
    def date_time_this_century(self, before_now: bool = True, after_now: bool = False, tzinfo: Optional[TzInfo] = None) -> datetime: ...
    def date_time_this_decade(self, before_now: bool = True, after_now: bool = False, tzinfo: Optional[TzInfo] = None) -> datetime: ...
    def date_time_this_year(self, before_now: bool = True, after_now: bool = False, tzinfo: Optional[TzInfo] = None) -> datetime: ...
    def date_time_this_month(self, before_now: bool = True, after_now: bool = False, tzinfo: Optional[TzInfo] = None) -> datetime: ...
    def date_this_century(self, before_today: bool = True, after_today: bool = False) -> dtdate: ...
    def date_this_decade(self, before_today: bool = True, after_today: bool = False) -> dtdate: ...
    def date_this_year(self, before_today: bool = True, after_today: bool = False) -> dtdate: ...
    def date_this_month(self, before_today: bool = True, after_today: bool = False) -> dtdate: ...
    def time_series(self, start_date: DateParseType = '-30d', end_date: DateParseType = 'now', precision: Optional[float] = None, distrib: Optional[Callable[[datetime], float]] = None, tzinfo: Optional[TzInfo] = None) -> Iterator[Tuple[datetime, Any]]: ...
    def am_pm(self) -> str: ...
    def day_of_month(self) -> str: ...
    def day_of_week(self) -> str: ...
    def month(self) -> str: ...
    def month_name(self) -> str: ...
    def year(self) -> str: ...
    def century(self) -> str: ...
    def timezone(self) -> str: ...
    def pytimezone(self, *args: Any, **kwargs: Any) -> Optional[TzInfo]: ...
    def date_of_birth(self, tzinfo: Optional[TzInfo] = None, minimum_age: int = 0, maximum_age: int = 115) -> dtdate: ...

def convert_timestamp_to_datetime(timestamp: Union[int, float], tzinfo: TzInfo) -> datetime: ...
