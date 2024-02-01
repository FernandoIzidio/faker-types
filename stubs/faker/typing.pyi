import dataclasses
from _typeshed import Incomplete
from datetime import date, datetime, timedelta
from typing import Sequence, Union, Type

DateParseType = Union[date, datetime, timedelta, str, int]
HueType = Union[str, float, int, Sequence[int]]
SexLiteral: str
SeedType = Union[int, float, str, bytes, bytearray, None]

@dataclasses.dataclass
class Country:
    name: str
    timezones: Sequence[str]
    alpha_2_code: str
    alpha_3_code: str
    continent: str
    capital: str
    def __init__(self, name, timezones, alpha_2_code, alpha_3_code, continent, capital) -> None: ...
