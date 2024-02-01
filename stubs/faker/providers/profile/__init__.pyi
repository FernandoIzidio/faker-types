from .. import BaseProvider as BaseProvider
from ...typing import SexLiteral as SexLiteral
from datetime import date
from decimal import Decimal
from typing import Dict, List, Optional, Tuple, Union

class Provider(BaseProvider):
    def simple_profile(self, sex: Optional[SexLiteral] = None) -> Dict[str, Union[str, date, SexLiteral]]: ...
    def profile(self, fields: Optional[List[str]] = None, sex: Optional[SexLiteral] = None) -> Dict[str, Union[str, Tuple[Decimal, Decimal], List[str], date]]: ...
