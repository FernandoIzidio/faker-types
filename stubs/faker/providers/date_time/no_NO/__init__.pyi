from .. import Provider as DateTimeProvider
from _typeshed import Incomplete

class Provider(DateTimeProvider):
    MONTH_NAMES: Incomplete
    DAY_NAMES: Incomplete
    def day_of_week(self) -> str: ...
    def month_name(self) -> str: ...
