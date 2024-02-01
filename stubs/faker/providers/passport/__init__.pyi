import datetime
from .. import BaseProvider as BaseProvider, ElementsType as ElementsType
from typing import Tuple

localized: bool

class Provider(BaseProvider):
    passport_number_formats: ElementsType
    def passport_dob(self) -> datetime.date: ...
    def passport_owner(self, gender: str = 'X') -> Tuple[str, str]: ...
    def passport_number(self) -> str: ...
