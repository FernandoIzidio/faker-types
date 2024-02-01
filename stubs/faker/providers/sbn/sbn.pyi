from _typeshed import Incomplete
from typing import Any, Optional

class SBN:
    MAX_LENGTH: int
    registrant: Incomplete
    publication: Incomplete
    def __init__(self, registrant: Optional[str] = None, publication: Optional[str] = None) -> None: ...

class SBN9(SBN):
    check_digit: Incomplete
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def format(self, separator: str = '') -> str: ...
