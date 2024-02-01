from .. import Provider as SsnProvider
from _typeshed import Incomplete
from string import ascii_uppercase

ALPHABET = ascii_uppercase
ALPHANUMERICS: Incomplete
ALPHANUMERICS_DICT: Incomplete
MONTHS_LIST: Incomplete
VOWELS: str
CONSONANTS: Incomplete
MUNICIPALITIES_LIST: Incomplete
CHECKSUM_TABLE: Incomplete

def checksum(value: str) -> str: ...

class Provider(SsnProvider):
    def ssn(self) -> str: ...
    vat_id_formats: Incomplete
    def vat_id(self) -> str: ...
    @staticmethod
    def is_leap_year(year: int) -> bool: ...
