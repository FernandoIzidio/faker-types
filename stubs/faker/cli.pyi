from . import VERSION as VERSION,  Faker as Faker, documentor as documentor, exceptions as exceptions
from .config import AVAILABLE_LOCALES as AVAILABLE_LOCALES, DEFAULT_LOCALE as DEFAULT_LOCALE, META_PROVIDERS_MODULES as META_PROVIDERS_MODULES
from .documentor import Documentor as Documentor
from .providers import BaseProvider as BaseProvider
from _typeshed import Incomplete
from io import TextIOWrapper
from typing import Dict, List, Optional, TextIO, TypeVar, Union

T = TypeVar('T')

def print_provider(doc: Documentor, provider: BaseProvider, formatters: Dict[str, T], excludes: Optional[List[str]] = None, output: Optional[TextIO] = None) -> None: ...
def print_doc(provider_or_field: Optional[str] = None, args: Optional[List[T]] = None, lang: str = ..., output: Optional[Union[TextIO, TextIOWrapper]] = None, seed: Optional[float] = None, includes: Optional[List[str]] = None) -> None: ...

class Command:
    argv: Optional[str]
    prog_name: str
    def __init__(self, argv: Optional[str] = None) -> None: ...
    def execute(self) -> None: ...

def execute_from_command_line(argv: Optional[str] = None) -> None: ...
