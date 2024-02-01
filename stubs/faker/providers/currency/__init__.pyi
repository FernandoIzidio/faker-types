from .. import BaseProvider as BaseProvider, ElementsType as ElementsType
from typing import Dict, Optional, Tuple

localized: bool

class Provider(BaseProvider):
    currencies: ElementsType[Tuple[str, str]]
    cryptocurrencies: ElementsType[Tuple[str, str]]
    currency_symbols: Dict[str, str]
    price_formats: ElementsType[str]
    def currency(self) -> Tuple[str, str]: ...
    def currency_code(self) -> str: ...
    def currency_name(self) -> str: ...
    def currency_symbol(self, code: Optional[str] = None) -> str: ...
    def cryptocurrency(self) -> Tuple[str, str]: ...
    def cryptocurrency_code(self) -> str: ...
    def cryptocurrency_name(self) -> str: ...
    def pricetag(self) -> str: ...
