from .. import Provider as DateTimeProvider
from _typeshed import Incomplete
from faker.typing import Country as Country

class Provider(DateTimeProvider):
    DAY_NAMES: Incomplete
    MONTH_NAMES: Incomplete
    countries: Incomplete
    def day_of_week(self) -> str: ...
    def month_name(self) -> str: ...
