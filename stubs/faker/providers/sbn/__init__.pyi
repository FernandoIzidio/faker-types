from .. import BaseProvider as BaseProvider
from .rules import RULES as RULES
from .sbn import SBN as SBN, SBN9 as SBN9
from faker.providers.sbn.rules import RegistrantRule as RegistrantRule

class Provider(BaseProvider):
    def sbn9(self, separator: str = '-') -> str: ...
