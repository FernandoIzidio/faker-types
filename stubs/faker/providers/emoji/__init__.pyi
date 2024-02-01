from .. import BaseProvider as BaseProvider
from _typeshed import Incomplete

class Provider(BaseProvider):
    emojis: Incomplete
    emoji_formats: str
    def emoji(self) -> str: ...
