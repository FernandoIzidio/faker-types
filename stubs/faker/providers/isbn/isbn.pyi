from _typeshed import Incomplete
from typing import Any, Optional

class ISBN:
    MAX_LENGTH: int
    ean: Incomplete
    group: Incomplete
    registrant: Incomplete
    publication: Incomplete
    def __init__(self, ean: Optional[str] = None, group: Optional[str] = None, registrant: Optional[str] = None, publication: Optional[str] = None) -> None: ...

class ISBN13(ISBN):
    check_digit: Incomplete
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def format(self, separator: str = '') -> str: ...

class ISBN10(ISBN):
    check_digit: Incomplete
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def format(self, separator: str = '') -> str: ...
