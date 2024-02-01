from .. import Provider as SsnProvider
from _typeshed import Incomplete

class Provider(SsnProvider):
    characters: Incomplete
    numbers: Incomplete
    all_characters: Incomplete
    def ssn(self) -> str: ...
