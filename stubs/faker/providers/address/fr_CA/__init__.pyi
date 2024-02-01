from ..en_CA import Provider as EnCaProvider
from _typeshed import Incomplete
from typing import Any

class Provider(EnCaProvider):
    city_prefixes: Incomplete
    city_suffixes: Incomplete
    street_prefixes: Incomplete
    provinces: Incomplete
    street_name_formats: Incomplete
    city_formats: Incomplete
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def street_prefix(self) -> str: ...
