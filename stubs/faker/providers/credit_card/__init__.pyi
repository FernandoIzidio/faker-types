from .. import BaseProvider as BaseProvider
from ...typing import DateParseType as DateParseType
from _typeshed import Incomplete
from typing import Dict, List, Optional, TypeVar

localized: bool
CardType = TypeVar('CardType', 'CreditCard', str)

class CreditCard:
    name: Incomplete
    prefixes: Incomplete
    length: Incomplete
    security_code: Incomplete
    security_code_length: Incomplete
    def __init__(self, name: str, prefixes: List[str], length: int = 16, security_code: str = 'CVC', security_code_length: int = 3) -> None: ...

class Provider(BaseProvider):
    prefix_maestro: List[str]
    prefix_mastercard: List[str]
    prefix_visa: List[str]
    prefix_amex: List[str]
    prefix_discover: List[str]
    prefix_diners: List[str]
    prefix_jcb16: List[str]
    prefix_jcb15: List[str]
    credit_card_types: Dict[str, CreditCard]
    luhn_lookup: Incomplete
    def credit_card_provider(self, card_type: Optional[CardType] = None) -> str: ...
    def credit_card_number(self, card_type: Optional[CardType] = None) -> str: ...
    def credit_card_expire(self, start: DateParseType = 'now', end: DateParseType = '+10y', date_format: str = '%m/%y') -> str: ...
    def credit_card_full(self, card_type: Optional[CardType] = None) -> str: ...
    def credit_card_security_code(self, card_type: Optional[CardType] = None) -> str: ...
