from .. import BaseProvider as BaseProvider
from typing import Tuple, Union

localized: bool
PrefixType = Tuple[Union[int, str, Tuple[Union[int, str], ...]], ...]

class Provider(BaseProvider):
    local_prefixes: PrefixType
    def ean(self, length: int = 13, prefixes: PrefixType = ()) -> str: ...
    def ean8(self, prefixes: PrefixType = ()) -> str: ...
    def ean13(self, prefixes: PrefixType = ()) -> str: ...
    def localized_ean(self, length: int = 13) -> str: ...
    def localized_ean8(self) -> str: ...
    def localized_ean13(self) -> str: ...
