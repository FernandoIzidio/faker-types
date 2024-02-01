from .. import Provider as PassportProvider
from _typeshed import Incomplete
from datetime import date
from typing import Tuple

class Provider(PassportProvider):
    passport_number_formats: Incomplete
    def passport_dates(self, birthday: date = ...) -> Tuple[str, str, str]: ...
    def passport_gender(self, seed: int = 0) -> str: ...
    def passport_full(self) -> str: ...
