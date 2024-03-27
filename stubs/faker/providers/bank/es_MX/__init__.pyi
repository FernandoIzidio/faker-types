from .. import Provider as BankProvider
from typing import Optional, Tuple

def get_clabe_control_digit(clabe: str) -> int: ...
def is_valid_clabe(clabe: str) -> bool: ...

class Provider(BankProvider):
    banks: Tuple[str, ...]
    bank_codes: Tuple[int, ...]
    def bank(self) -> str: ...
    def clabe(self, bank_code: Optional[int] = None) -> str: ...