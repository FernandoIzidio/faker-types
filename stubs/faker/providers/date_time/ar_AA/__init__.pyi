from .. import Provider as DateTimeProvider
from _typeshed import Incomplete
from faker.typing import Country as Country

class Provider(DateTimeProvider):
    DAY_NAMES: Incomplete
    MONTH_NAMES: Incomplete
    centuries: Incomplete
    countries: Incomplete
    AM_PM: Incomplete
    def month_name(self) -> str: ...
    def am_pm(self) -> str: ...
    def day_of_week(self) -> str: ...
