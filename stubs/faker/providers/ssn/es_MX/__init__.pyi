from .. import Provider as BaseProvider
from _typeshed import Incomplete
from typing import Optional
from typing_extensions import Literal

ALPHABET: Incomplete
ALPHANUMERIC: Incomplete
VOWELS: str
CONSONANTS: Incomplete
STATES_RENAPO: Incomplete
FORBIDDEN_WORDS: Incomplete
CURP_CHARACTERS: str

def ssn_checksum(digits: map) -> int: ...
def curp_checksum(characters: str) -> int: ...

class Provider(BaseProvider):
    ssn_formats: Incomplete
    def ssn(self) -> str: ...
    def curp(self) -> str: ...
    def rfc(self, natural: bool = True) -> str: ...
    def elector_code(self, gender: Optional[Literal['H', 'M']] = None) -> str: ...
