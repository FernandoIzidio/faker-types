from .config import AVAILABLE_LOCALES as AVAILABLE_LOCALES, DEFAULT_LOCALE as DEFAULT_LOCALE, PROVIDERS as PROVIDERS
from .generator import Generator as Generator
from .utils.loading import list_module as list_module
from _typeshed import Incomplete
from typing import Any, List, Optional
from logging import Logger

logger: Logger
inREPL: bool

class Factory:
    @classmethod
    def create(cls, locale: Optional[str] = None, providers: Optional[List[str]] = None, generator: Optional[Generator] = None, includes: Optional[List[str]] = None, use_weighting: bool = True, **config: Any) -> Generator: ...
