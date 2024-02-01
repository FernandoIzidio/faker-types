from .. import PrefixType as PrefixType, Provider as BarcodeProvider
from _typeshed import Incomplete
from typing import Optional, Pattern

class Provider(BarcodeProvider):
    local_prefixes: Incomplete
    upc_e_base_pattern: Pattern
    upc_ae_pattern1: Pattern
    upc_ae_pattern2: Pattern
    upc_ae_pattern3: Pattern
    def ean13(self, prefixes: PrefixType = (), leading_zero: Optional[bool] = None) -> str: ...
    def upc_a(self, upc_ae_mode: bool = False, base: Optional[str] = None, number_system_digit: Optional[int] = None) -> str: ...
    def upc_e(self, base: Optional[str] = None, number_system_digit: Optional[int] = None, safe_mode: bool = True) -> str: ...
