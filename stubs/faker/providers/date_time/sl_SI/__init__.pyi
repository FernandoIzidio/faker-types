from .. import Provider as DateTimeProvider
from _typeshed import Incomplete

class Provider(DateTimeProvider):
    DAY_NAMES: Incomplete
    MONTH_NAMES: Incomplete
    def day_of_week(self) -> str: ...
    def month_name(self) -> str: ...
