from .. import BaseProvider as BaseProvider
from .isbn import ISBN as ISBN, ISBN10 as ISBN10, ISBN13 as ISBN13
from .rules import RULES as RULES
from faker.providers.isbn.rules import RegistrantRule as RegistrantRule

class Provider(BaseProvider):
    def isbn13(self, separator: str = '-') -> str: ...
    def isbn10(self, separator: str = '-') -> str: ...
