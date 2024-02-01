from .generator import Generator as Generator
from .providers import BaseProvider as BaseProvider
from .proxy import Faker as Faker
from _typeshed import Incomplete
from enum import Enum, auto
from typing import Any, Dict, List, Optional, Tuple, Union

class FakerEnum(Enum):
    A = auto
    B = auto

class Documentor:
    generator: Union[Generator, Faker]
    max_name_len: int
    already_generated: List[str]
    def __init__(self, generator: Union[Generator, Faker]) -> None: ...
    def get_formatters(self, locale: Optional[str] = None, excludes: Optional[List[str]] = None, **kwargs: Any) -> List[Tuple[BaseProvider, Dict[str, str]]]: ...
    def get_provider_formatters(self, provider: BaseProvider, prefix: str = 'fake.', with_args: bool = True, with_defaults: bool = True) -> Dict[str, str]: ...
    @staticmethod
    def get_provider_name(provider_class: BaseProvider) -> str: ...
