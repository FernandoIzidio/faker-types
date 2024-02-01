from .. import Provider as BankProvider
from _typeshed import Incomplete
from typing import Optional

class Provider(BankProvider):
    bban_format: str
    country_code: str
    swift_location_codes: Incomplete
    swift_branch_codes: Incomplete
    def swift8(self, use_dataset: bool = True) -> str: ...
    def swift11(self, primary: bool = False, use_dataset: bool = True) -> str: ...
    def swift(self, length: Optional[int] = None, primary: bool = False, use_dataset: bool = True) -> str: ...
